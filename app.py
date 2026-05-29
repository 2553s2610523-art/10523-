import datetime
import streamlit as st

# 웹앱 제목
st.title("📅 수행평가 마감 알람이")
st.subheader("놓치기 쉬운 수행평가 일정, 한눈에 관리하세요!")

# 구분선
st.divider()

# 오늘 날짜 표시
today = datetime.date.today()
st.info(f"📆 오늘은 **{today.year}년 {today.month}월 {today.day}일** 입니다.")

# 수행평가 과목 선택
subject = st.selectbox(
    "과목을 선택하세요:",
    ["국어 수행평가", "수학 수행평가", "영어 수행평가", "과학 탐구보고서", "사회 발표준비"]
)

# 마감일 지정 (기본값은 오늘 날짜)
deadline = st.date_input("마감일을 선택하세요:", today)

# 디데이 계산 및 출력
if deadline:
    # 날짜 차이 계산
    d_day = (deadline - today).days
    
    st.write("---")
    if d_day > 0:
        st.success(f"🚨 **{subject}** 마감까지 **{d_day}일** 남았습니다. 미리미리 준비하세요!")
    elif d_day == 0:
        st.error(f"🔥 **{subject}** 마감일이 **오늘(D-Day)** 입니다! 지금 당장 제출하세요!")
    else:
        st.warning(f"✅ **{subject}** 마감일이 **{-d_day}일** 지났습니다. 제출 여부를 확인하세요.")

# 사이드바 응원 문구
st.sidebar.markdown("### ✍️ 고등학생 필승 다짐")
st.sidebar.write("벼락치기는 이제 그만!")
st.sidebar.info("체계적인 관리로 수행평가 만점 받자! 💯")
