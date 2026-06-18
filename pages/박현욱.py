import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="예체능 수행평가 알리미",
    page_icon="🎨",
    layout="centered"
)

# 헤더 구역
st.title("🎨🎵🏃 예체능 수행평가 알리미")
st.markdown("미술, 음악, 체육 과목의 수행평가 일정과 준비물을 한눈에 확인하세요!")
st.markdown("---")

# 가상의 수행평가 데이터 데이터베이스 (실제 데이터로 변경 가능)
@st.cache_data
def load_data():
    data = [
        {
            "과목": "미술",
            "평가 주제": "아크릴 정물화 채색",
            "마감일": "2026-07-02",
            "준비물": "아크릴 물감 세트, 붓, 붓통, 헝겊",
            "평가 기준": "색채 조화(40%), 완성도(40%), 표현력(20%)"
        },
        {
            "과목": "음악",
            "평가 주제": "리코더 중주 (할아버지의 11개월)",
            "마감일": "2026-06-25",
            "준비물": "알토 리코더, 악보",
            "평가 기준": "박자 및 음정(50%), 호흡 및 아티큘레이션(30%), 팀 협력(20%)"
        },
        {
            "과목": "체육",
            "평가 주제": "배드민턴 하이클리어 및 서브",
            "마감일": "2026-06-30",
            "준비물": "체육복, 운동화 (라켓은 학교 지급)",
            "평가 기준": "자세의 정확성(50%), 목표 구역 안착률(50%)"
        }
    ]
    return pd.DataFrame(data)

df = load_data()
df["마감일"] = pd.to_datetime(df["마감일"])

# 디데이 계산 함수
def calculate_dday(target_date):
    today = datetime.now().date()
    delta = (target_date.date() - today).days
    if delta == 0:
        return "🔥 D-Day"
    elif delta > 0:
        return f"⏳ D-{delta}"
