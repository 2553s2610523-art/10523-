import streamlit as dt
import datetime
import pandas as pd

# 1. 페이지 기본 설정 및 스타일
dt.set_page_config(
    page_title="과·과탐·기가 수행평가 알림장",
    page_icon="📅",
    layout="wide"
)

# 데이터 보관을 위한 세션 상태 초기화 (빈 상태로 시작)
if "evaluations" not in dt.session_state:
    dt.session_state.evaluations = []
if "id_counter" not in dt.session_state:
    dt.session_state.id_counter = 1

# 앱 타이틀 구역
dt.title("🎒 예정된 수행평가 알림장")
dt.markdown("과학 · 과학탐구실험 · 기술·가정 과목의 수행평가를 기록하고 관리하세요!")
dt.markdown("---")

# 레이아웃 분할: 왼쪽 (입력 창) | 오른쪽 (확인 및 삭제 창)
left_col, right_col = dt.columns([1, 2])

# ==========================================
# 왼쪽 사이드: 수행평가 등록 창
# ==========================================
with left_col:
    dt.subheader("📝 새 수행평가 등록")
    
    with dt.form("add_form", clear_on_submit=True):
        # 과목 선택 (지정된 3개 과목 한정)
        subject = dt.selectbox("과목 선택", ["과학", "과학탐구실험", "기술·가정"])
        
        # 수행평가 이름 (예시 표시 제거)
        title = dt.text_input("수행평가 이름")
        
        # 마감일 (오늘 이후부터 선택 가능하도록 설정)
        due_date = dt.date_input("마감일", datetime.date.today())
        
        # 세부 내용 (예시 표시 제거)
        content = dt.text_area("세부 내용")
        
        # 등록 버튼
        submit_button = dt.form_submit_button("📅 일정 등록하기")
        
        if submit_button:
            if not title.strip():
                dt.error("수행평가 이름을 입력해주세요!")
            else:
                # 데이터 추가
                new_data = {
                    "id": dt.session_state.id_counter,
                    "subject": subject,
                    "title": title,
                    "due_date": due_date,
                    "content": content
                }
                dt.session_state.evaluations.append(new_data)
                dt.session_state.id_counter += 1
                dt.toast(f"✅ {subject} 수행평가가 등록되었습니다!", icon="🎉")
                dt.rerun()

# ==========================================
# 오른쪽 사이드: 수행평가 확인 및 삭제 창
# ==========================================
with right_col:
    dt.subheader("🔔 다가오는 수행평가 목록")
    
    if not dt.session_state.evaluations:
        dt.info("현재 등록된 수행평가 일정이 없습니다. 새로운 일정을 등록해 보세요! ✨")
    else:
        # 마감일 순으로 정렬하기 위해 데이터프레임 변환 후 정렬
        df = pd.DataFrame(dt.session_state.evaluations)
        df = df.sort_values(by="due_date").to_dict('records')
        
        # 정렬된 데이터를 화면에 표시
        for idx, item in enumerate(df):
            # D-Day 계산
            today = datetime.date.today()
            d_day = (item['due_date'] - today).days
            
            if d_day == 0:
                d_day_str = "🔥 D-Day (오늘 마감)"
                color = "red"
            elif d_day < 0:
                d_day_str = f"❌ 마감일 경과 ({abs(d_day)}일 지남)"
                color = "gray"
            else:
                d_day_str = f"⏳ D-{d_day}"
                color = "blue"
                
            # 과목별 이모지 설정
            emoji = "🔬" if item['subject'] == "과학" else "🧪" if item['subject'] == "과학탐구실험" else "🏠"
            
            # 컨테이너 스타일링 효과 및 정보 표시
            with dt.container(border=True):
                # 헤더 부분 (과목, 제목, 삭제 버튼을 한 줄에 배치)
                title_col, btn_col = dt.columns([5, 1])
                
                with title_col:
                    dt.markdown(f"### {emoji} [{item['subject']}] {item['title']}")
                with btn_col:
                    # 각 아이템별 고유한 삭제 버튼 생성
                    if dt.button("🗑️ 삭제", key=f"del_{item['id']}"):
                        # session_state에서 해당 id 데이터 삭제
                        dt.session_state.evaluations = [e for e in dt.session_state.evaluations if e['id'] != item['id']]
                        dt.toast("선택한 일정을 삭제했습니다.", icon="🗑️")
                        dt.rerun() # 화면 즉시 갱신
                
                # 마감일 및 세부 내용 표시
                dt.markdown(f"**마감일:** {item['due_date']}  |  **남은 기간:** :{color}[**{d_day_str}**]")
                if item['content'].strip():
                    dt.info(item['content'])
