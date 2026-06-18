import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="예체능 수행평가 알리미",
    page_icon="🎨",
    layout="wide"
)

# 헤더 부분
st.title("🎨🎵🏃‍♂️ 예체능 수행평가 알리미")
st.markdown("미술, 음악, 체육 과목의 수행평가 일정과 준비물을 놓치지 않게 도와주는 알리미입니다.")

# 샘플 데이터 생성
@st.cache_data
def load_data():
    data = {
        "과목": ["미술", "음악", "체육", "미술", "음악", "체육"],
        "평가 항목": ["아크릴 풍경화 그리기", "가창 (한국 가곡)", "배드민턴 하이클리어", "현대 미술 감상문", "기탁 악기 연주 (리코더)", "체력 측정 (PAPS)"],
        "마감일": ["2026-06-25", "2026-06-28", "2026-07-02", "2026-07-05", "2026-07-10", "2026-07-15"],
        "반영 비율": ["30%", "20%", "40%", "20%", "30%", "30%"],
        "준비물/참고사항": ["아크릴 물감, 붓, 캔버스(학교 제공)", "교과서 가창곡 중 택1, 암보 필수", "편한 체육복, 운동화 착용", "지정 도서 읽고 오기", "개인 리코더 지참", "최선을 다할 마음가짐!"]
    }
    df = pd.DataFrame(data)
    df["마감일"] = pd.to_datetime(df["마감일"])
    return df

df = load_data()

# 사이드바 - 필터링 기능
st.sidebar.header("🔍 필터 및 검색")
subjects = ["전체"] + list(df["과목"].unique())
selected_subject = st.sidebar.selectbox("과목 선택", subjects)

# 데이터 필터링
if selected_subject != "전체":
    filtered_df = df[df["과목"] == selected_subject]
else:
    filtered_df = df

# 오늘 날짜 기준 D-Day 계산 및 정렬
filtered_df = filtered_df.sort_values(by="마감일")
today = datetime.today()
filtered_df["D-Day"] = (filtered_df["마감일"] - today).dt.days

# D-Day 포맷팅 함수
def format_dday(days):
    if days < 0:
        return f"마감 완료 ({-days}일 지남)"
    elif days == 0:
        return "🔥 오늘 마감!"
    else:
        return f"D-{days}"

filtered_df["남은 기간"] = filtered_df["D-Day"].apply(format_dday)

# 메인 화면 구성
st.subheader("📅 수행평가 일정표")

# 표 출력을 위해 날짜 형식 변경
display_df = filtered
