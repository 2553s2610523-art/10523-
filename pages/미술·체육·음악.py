import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="예체능 수행평가 알리미", page_icon="🎨", layout="centered")

# 세션 상태(Session State)를 이용해 데이터 유지
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"과목": "🎨 미술", "평가 내용": "소묘 수행평가", "마감일": datetime(2026, 7, 5).date()},
        {"과목": "🎵 음악", "평가 내용": "가창 시험 (자유곡)", "마감일": datetime(2026, 7, 8).date()},
        {"과목": "🏃 체육", "평가 내용": "배드민턴 서브 측정", "마감일": datetime(2026, 6, 30).date()},
    ]

# 제목 영역
st.title("🎨 🎵 🏃 예체능 수행평가 알리미")
st.write("미술, 음악, 체육 수행평가 일정을 한눈에 관리하고 D-Day를 확인하세요!")
st.markdown("---")

# 1. 수행평가 추가하기 (사이드바)
st.sidebar.header("➕ 새로운 수행평가 등록")
subject = st.sidebar.selectbox("과목 선택", ["🎨 미술", "🎵 음악", "🏃 체육"])
content = st.sidebar.text_input("평가 내용", placeholder="예: 축구 드리블 테스트")
due_date = st.sidebar.date_input("마감일", datetime.now().date())

if st.sidebar.button("등록하기"):
    if content.strip() == "":
        st.sidebar.error("평가 내용을 입력해주세요!")
    else:
        st.session_state.tasks.append({"과목": subject, "평가 내용": content, "마감일": due_date})
        st.sidebar.success("성공적으로 등록되었습니다!")
        st.rerun()

# 2. 수행평가 목록 및 D-Day 계산
st.subheader("📅 현재 남은 수행평가 일정")

if not st.session_state.tasks:
    st.info("남은 수행평가 일정이 없습니다. 사이드바에서 새로 등록해보세요!")
else:
    # 데이터를 표 형태로 변환하기 위한 리스트 생성
    display_data = []
    today = datetime.now().date()

    for idx, task in enumerate(st.session_state.tasks):
        d_day_num = (task["마감일"] - today).days
        
        # D-Day 표시 형식 설정
        if d_day_num == 0:
            d_day_str = "🔥 D-Day"
        elif d_day_num < 0:
            d_day_str = f"✅ 완료 ({abs(d_day_num)}일 지남)"
        else:
            d_day_str = f"⏳ D-{d_day_num}"
            
        display_data.append({
            "번호": idx + 1,
            "과목": task["과목"],
            "평가 내용": task["평가 내용"],
            "마감일": task["마감일"].strftime("%Y-%m-%d"),
            "남은 기간": d_day_str
        })

    # 데이터프레임 생성 및 출력
    df = pd.DataFrame(display_data)
    st.dataframe(df.set_index("번호"), use_container_width=True)

    # 3. 수행평가 삭제 기능
    st.markdown("---")
    st.subheader("🗑️ 수행평가 삭제/완료 처리")
    delete_idx = st.number_input("삭제할 수행평가의 번호를 선택하세요.", min_value=1, max_value=len(st.session_state.tasks), step=1)
    
    if st.button("선택한 항목 삭제"):
        st.session_state.tasks.pop(delete_idx - 1)
        st.success("항목이 삭제되었습니다.")
        st.rerun()
