import streamlit as st
import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="수행평가 알리미",
    page_icon="🔥",
    layout="centered"
)

# 스트림릿 자체에서 폭죽 효과를 내기 위한 컴포넌트 호출 함수
def trigger_celebration():
    st.balloons()  # 기본 풍선 효과
    st.snow()      # 축하 효과를 위한 추가 시각 효과

# 앱 제목
st.title("📚 국어·수학·영어 수행평가 알리미")
st.markdown("---")

# 세션 상태(Session State)를 활용해 과목별 마감일 초기화 (테스트용 기본값 설정)
if 'dates' not in st.session_state:
    today = datetime.date.today()
    st.session_state.dates = {
        "국어": today + datetime.timedelta(days=8),  # 8일 남음 (잔잔함)
        "수학": today + datetime.timedelta(days=3),  # 3일 남음 (거셈)
        "영어": today,                               # 오늘 마감 (폭죽 및 폭발)
    }

# 1. 과목 선택 탭 생성
tab1, tab2, tab3 = st.tabs(["📝 국어", "📐 수학", "🔤 영어"])

def render_subject_ui(subject_name):
    st.subheader(f"{subject_name} 수행평가 상태")
    
    # 마감일 수정 기능
    chosen_date = st.date_input(
        f"{subject_name} 마감일 변경", 
        st.session_state.dates[subject_name],
        key=f"date_{subject_name}"
    )
    st.session_state.dates[subject_name] = chosen_date
    
    # 디데이 계산
    today = datetime.date.today()
    remaining_days = (chosen_date - today).days
    
    # 디데이 및 불꽃 효과 조건문
    if remaining_days < 0:
        st.error(f"지나간 수행평가입니다. (종료된 지 {abs(remaining_days)}일째)")
        st.markdown("<h1 style='text-align: center; color: #555555;'>⚫ 재만 남은 불꽃</h1>", unsafe_allow_html=True)
        
    elif remaining_days == 0:
        st.success("🎉 오늘이 마감일입니다! 파이팅! 🎉")
        st.markdown("<h1 style='text-align: center; font-size: 80px; animation: blink 1s infinite;'>💥</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #FF3333;'>당장 제출하세요! 폭발하는 불꽃</h3>", unsafe_allow_html=True)
        # 당일이 되면 폭죽 효과 실행
        trigger_celebration()
        
    elif remaining_days <= 2:
        st.warning(f"⚠️ 마감 임박! D-{remaining_days}")
        # HTML/CSS를 이용해 크고 거친 불꽃 시각화 (크기 70px, 그림자 강하게)
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 20px 0;">
                <div style="font-size: 70px; text-shadow: 0 0 30px #FF3333, 0 0 50px #FF6600; animation: pulse 0.5s infinite alternate;">🔥</div>
                <h4 style="color: #FF3333; margin-top: 10px;">💥💥💥 위태롭고 거칠게 타오르는 폭발 직전!</h4>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    elif remaining_days <= 6:
        st.info(f"💡 준비 시작하세요! D-{remaining_days}")
        # 중간 크기 불꽃 (크기 45px, 그림자 중간)
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 20px 0;">
                <div style="font-size: 45px; text-shadow: 0 0 15px #FF6600;">🔥</div>
                <h4 style="color: #FF6600; margin-top: 10px;">🔥🔥 거세고 흔들리는 불꽃!</h4>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    else:
        st.info(f"✅ 아직 여유가 있습니다. D-{remaining_days}")
        # 작은 불꽃 (크기 25px)
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 20px 0;">
                <div style="font-size: 25px; text-shadow: 0 0 5px #FFCC00;">🔥</div>
                <h4 style="color: #FFCC00; margin-top: 10px;">🔥 잔잔하고 안정적인 불꽃</h4>
            </div>
            """, 
            unsafe_allow_html=True
        )

# 각 탭에 UI 렌더링
with tab1:
    render_subject_ui("국어")
with tab2:
    render_subject_ui("수학")
with tab3:
    render_subject_ui("영어")
