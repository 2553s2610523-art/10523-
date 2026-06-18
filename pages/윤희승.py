import streamlit as tf
import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="수행평가 알리미", page_icon="📅", layout="wide")

# 1. 과목 리스트 정의 (요청하신 과목 구성)
SUBJECTS = ["과학", "국어", "수학", "영어", "기가", "정보", "미술", "과탐", "사회", "음악", "체육", "한국사"]

# 2. 데이터 저장을 위한 Session State 초기화
if "evaluations" not in st.session_state:
    # 기본 샘플 데이터 제공
    st.session_state.evaluations = [
        {"과목": "수학", "수행평가명": "미적분 문제 풀이 제출", "마감일": datetime(2026, 6, 25).date(), "내용": "교과서 120p~135p 풀이 노트 제출"},
        {"과목": "과학", "수행평가명": "물리 실험 보고서", "마감일": datetime(2026, 6, 20).date(), "내용": "자유 낙하 실험 결과 분석 보고서"},
    ]

st.title("📅 수행평가 알리미 앱")
st.markdown("나의 수행평가 일정을 기록하고 디데이(D-Day)를 확인하세요!")

# 사이드바: 새로운 수행평가 추가 폼
st.sidebar.header("➕ 새로운 수행평가 등록")
with st.sidebar.form(key="eval_form", clear_on_submit=True):
    sub = st.selectbox("과목 선택", SUBJECTS)
    title = st.text_input("수행평가명", placeholder="예: 영작문 에세이 제출")
    due_date = st.date_input("마감일", datetime.now().date())
    content = st.text_area("세부 내용 및 준비물", placeholder="내용을 입력하세요.")
    
    submit_button = st.form_submit_button(label="추가하기")
    
    if submit_button:
        if title:
            new_data = {"과목": sub, "수행평가명": title, "마감일": due_date, "내용": content}
            st.session_state.evaluations.append(new_data)
            st.sidebar.success(f"'{title}' 일정이 추가되었습니다!")
        else:
            st.sidebar.error("수행평가명을 입력해주세요.")

# 메인 화면: 등록된 수행평가 리스트 출력
st.subheader("📋 예정된 수행평가 목록")

if st.session_state.evaluations:
    # DataFrame으로 변환하여 시각화 및 관리
    df = pd.DataFrame(st.session_state.evaluations)
    
    # 디데이 계산 함수 적용
    today = datetime.now().date()
    
    def calculate_dday(due):
        # 만약 due가 문자열로 변환되어 있다면 date 객체로 변환
        if isinstance(due, str):
            due = datetime.strptime(due, "%Y-%m-%d").date()
        delta = (due - today).days
        if delta == 0:
            return "🔥 D-Day"
        elif delta < 0:
            return f"❌ 마감 ({abs(delta)}일 지남)"
        else:
            return f"⏳ D-{delta}"

    df["남은 기간 (D-Day)"] = df["마감일"].apply(calculate_dday)
    
    # 보기 좋게 컬럼 순서 재배치
    df = df[["남은 기간 (D-Day)", "과목", "수행평가명", "마감일", "내용"]]
    
    # 날짜 정렬 (마감일이 가까운 순서대로)
    df = df.sort_values(by="마감일")

    # 데이터 프레임 출력
    st.dataframe(df, use_container_width=True, hide_index=True)

    # 개별 상세 보기 및 삭제 기능
    st.markdown("---")
    st.subheader("🔍 세부 내용 확인 및 삭제")
    
    # 삭제 및 확인을 위한 선택 상자
    eval_titles = [f"[{item['과목']}] {item['수행평가명']}" for item in st.session_state.evaluations]
    selected_eval = st.selectbox("확인하거나 삭제할 수행평가를 선택하세요.", eval_titles)
    
    if selected_eval:
        # 선택한 인덱스 찾기
        idx = eval_titles.index(selected_eval)
        target = st.session_state.evaluations[idx]
        
        col1, col2 = st.columns([4, 1])
        with col1:
            st.info(f"**📝 세부 내용:** {target['내용'] if target['내용'] else '등록된 세부 내용이 없습니다.'}")
        with col2:
            if st.button("🗑️ 해당 일정 삭제", use_container_width=True):
                st.session_state.evaluations.pop(idx)
                st.rerun()

else:
    st.info("현재 등록된 수행평가가 없습니다. 왼쪽 사이드바에서 일정을 추가해보세요!")
