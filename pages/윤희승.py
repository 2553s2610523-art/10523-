import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(page_title="사회·한국사·정보 수행평가 알리미", page_icon="📅", layout="wide")

# 1. 지정된 3개 과목 설정
SUBJECTS = ["사회", "한국사", "정보"]

# 2. 데이터 저장을 위한 Session State 초기화 (샘플 데이터 포함)
if "evaluations" not in st.session_state:
    st.session_state.evaluations = [
        {"과목": "정보", "수행평가명": "파이썬 프로그래밍 과제 제출", "마감일": datetime(2026, 6, 25).date(), "내용": "반복문을 활용한 프로그램 소스코드 및 보고서 제출"},
        {"과목": "한국사", "수행평가명": "근현대사 인물 탐구 보고서", "마감일": datetime.now().date(), "내용": "자신이 선택한 인물의 업적과 평가를 A4 2장 이내로 작성 (오늘 마감!)"},
        {"과목": "사회", "수행평가명": "현대 사회 문제 토론 준비", "마감일": datetime(2026, 7, 2).date(), "내용": "기후변화 대응 방안에 대한 나의 입장 정리하기"}
    ]

# 3. 폭죽 효과 감지 로직 (오늘이 마감일인 수행평가가 있는지 확인)
today = datetime.now().date()
has_dday_today = any(item["마감일"] == today for item in st.session_state.evaluations)

if has_dday_today:
    st.balloons() # 조건 만족 시 폭죽(풍선) 효과 발동!
    st.toast("🔥 오늘 마감되는 수행평가가 있습니다! 서두르세요!", icon="🚨")

# --- UI 레이아웃 시작 ---
st.title("📅 사회 · 한국사 · 정보 수행평가 알리미")
st.markdown("중요한 수행평가 일정을 기록하고 마감일을 직관적으로 관리하세요.")

# 상단 대시보드 카드 형태 요약
st.markdown("### 📊 한눈에 보기")
dday_count = sum(1 for item in st.session_state.evaluations if item["마감일"] == today)
upcoming_count = sum(1 for item in st.session_state.evaluations if item["마감일"] > today)

col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.metric(label="🔥 오늘 마감 (D-Day)", value=f"{dday_count}개")
with col_info2:
    st.metric(label="⏳ 마감 예정", value=f"{upcoming_count}개")
with col_info3:
    st.metric(label="📚 총 등록 과제", value=f"{len(st.session_state.evaluations)}개")

st.markdown("---")

# 좌우 레이아웃 분할 (왼쪽: 목록 및 상세, 오른쪽: 신규 등록)
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📋 전체 수행평가 일정 리스트")
    
    if st.session_state.evaluations:
        # 데이터프레임 변환 및 디데이 계산
        df = pd.DataFrame(st.session_state.evaluations)
        
        def calculate_dday(due):
            if isinstance(due, str):
                due = datetime.strptime(due, "%Y-%m-%d").date()
            delta = (due - today).days
            if delta == 0:
                return "🚨 오늘 마감 (D-Day)"
            elif delta < 0:
                return f"❌ 마감 지남 (+{abs(delta)}일)"
            else:
                return f"⏳ D-{delta}"

        df["D-Day"] = df["마감일"].apply(calculate_dday)
        df = df[["D-Day", "과목", "수행평가명", "마감일", "내용"]]
        df = df.sort_values(by="마감일") # 마감일 임박순 정렬

        # 표 출력
        st.dataframe(df, use_container_width=True, hide_index=True)

        # 세부 내용 확인 및 삭제 섹션
        st.markdown("### 🔍 세부 내용 확인 및 삭제")
        eval_options = [f"[{item['과목']}] {item['수행평가명']}" for item in st.session_state.evaluations]
        selected_eval = st.selectbox("항목을 선택하면 상세 내용 확인 및 삭제가 가능합니다.", eval_options)
        
        if selected_eval:
            idx = eval_options.index(selected_eval)
            target = st.session_state.evaluations[idx]
            
            detail_col, btn_col = st.columns([4, 1])
            with detail_col:
                st.info(f"📌 **과제 상세 설명 및 준비물:**\n\n {target['내용'] if target['내용'] else '등록된 세부 내용이 없습니다.'}")
            with btn_col:
                st.markdown("<br>", unsafe_allow_html=True) # 줄바꿈 정렬
                if st.button("🗑️ 일정 삭제", use_container_width=True):
                    st.session_state.evaluations.pop(idx)
                    st.rerun()
    else:
        st.info("현재 등록된 수행평가 일정이 없습니다. 우측에서 새로 추가해 보세요!")

with right_col:
    st.subheader("➕ 수행평가 등록")
    with st.form(key="add_eval_form", clear_on_submit=True):
        sub = st.selectbox("과목", SUBJECTS)
        title = st.text_input("수행평가 내용/제목", placeholder="예: 파이썬 수행평가 제출")
        due_date = st.date_input("마감일 선택", datetime.now().date())
        content = st.text_area("상세 내용 (준비물, 범위 등)", placeholder="예: 패키지 모듈 리포트 작성")
        
        submit_btn = st.form_submit_button(label="알림 등록하기")
        
        if submit_btn:
            if title:
                new_data = {"과목": sub, "수행평가명": title, "마감일": due_date, "내용": content}
                st.session_state.evaluations.append(new_data)
                st.success(f"[{sub}] {title} 등록 완료!")
                st.rerun()
            else:
                st.error("수행평가 제목을 입력해 주세요.")
