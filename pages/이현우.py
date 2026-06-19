import streamlit as st
import datetime
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="과학·과탐·기가 수행평가 알림장",
    page_icon="📅",
    layout="centered"  # 일렬 배치를 위해 화면 중앙 집중형 레이아웃 채택
)

# 데이터 보관을 위한 세션 상태 초기화
if "evaluations" not in st.session_state:
    st.session_state.evaluations = []
if "id_counter" not in st.session_state:
    st.session_state.id_counter = 1

# 앱 헤더
st.title("🎒 과학·과탐·기가 수행평가 알림장")
st.markdown("과학 · 과학탐구실험 · 기술·가정 과목의 수행평가를 관리하는 공간입니다.")
st.markdown("---")

# ==========================================
# 1. [최상단] 수행평가 확인 및 삭제 창
# ==========================================
st.subheader("🔔 다가오는 수행평가 목록")

if not st.session_state.evaluations:
    st.info("현재 등록된 수행평가 일정이 없습니다. 아래에서 새로운 일정을 등록해 보세요! ✨")
else:
    # 마감일 순으로 정렬하기 위해 데이터프레임 변환 후 정렬
    df = pd.DataFrame(st.session_state.evaluations)
    df = df.sort_values(by="due_date").to_dict('records')
    
    # 정렬된 데이터를 화면에 표시
    for item in df:
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
        
        # 카드 스타일 컨테이너
        with st.container(border=True):
            # 과목/제목과 삭제 버튼 배치
            title_col, btn_col = st.columns([6, 1])
            
            with title_col:
                st.markdown(f"### {emoji} [{item['subject']}] {item['title']}")
            with btn_col:
                if st.button("🗑️ 삭제", key=f"del_{item['id']}"):
                    st.session_state.evaluations = [e for e in st.session_state.evaluations if e['id'] != item['id']]
                    st.toast("선택한 일정을 삭제했습니다.", icon="🗑️")
                    st.rerun()
            
            # 마감 정보 및 본문
            st.markdown(f"**마감일:** {item['due_date']}  |  **남은 기간:** :{color}[**{d_day_str}**]")
            if item['content'].strip():
                st.info(item['content'])

st.markdown("<br><br>", unsafe_allow_html=True) # 시각적인 구분을 위한 여백
st.markdown("---")

# ==========================================
# 2. [하단 배치] 새 수행평가 등록 기능
# ==========================================
st.subheader("📝 새 수행평가 추가하기")

with st.form("add_form", clear_on_submit=True):
    # 입력 항목들을 깔끔하게 두 줄로 정렬하기 위해 컬럼 분할
    col1, col2 = st.columns(2)
    
    with col1:
        subject = st.selectbox("과목 선택", ["과학", "과학탐구실험", "기술·가정"])
    with col2:
        due_date = st.date_input("마감일", datetime.date.today())
        
    title = st.text_input("수행평가 이름")
    content = st.text_area("세부 내용")
    
    submit_button = st.form_submit_button("일정 등록하기", use_container_width=True)
    
    if submit_button:
        if not title.strip():
            st.error("수행평가 이름을 입력해주세요")
        else:
            new_data = {
                "id": st.session_state.id_counter,
                "subject": subject,
                "title": title,
                "due_date": due_date,
                "content": content
            }
            st.session_state.evaluations.append(new_data)
            st.session_state.id_counter += 1
            st.toast(f"✅ {subject} 수행평가가 등록되었습니다", icon="🎉")
            st.rerun()
