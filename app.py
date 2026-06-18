 import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🧸 쉿! 수행평가 알림이 🩸",
    page_icon="🤡",
    layout="wide"
)

# [유아틱 + 소름돋는] 잔혹동화풍 Custom CSS
st.markdown("""
    <style>
    /* 유아틱한 핑크+스카이블루 그라데이션이지만 어딘가 어두운 느낌 */
    .stApp {
        background: linear-gradient(135deg, #ffdee9 0%, #b5fffc 100%);
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
    }
    
    /* 메인 타이틀: 알록달록하지만 피 흘리는 느낌의 붉은 그림자 */
    .creepy-title {
        font-size: 3.5rem !important;
        font-weight: 900;
        color: #ff4757;
        text-align: center;
        text-shadow: 3px 3px 0px #000000, 5px 5px 10px rgba(255, 0, 0, 0.5);
        margin-top: 20px;
        margin-bottom: 5px;
    }
    
    /* 서브 타이틀: 삐뚤빼뚤 유치원 글씨체 느낌과 경고문 */
    .creepy-sub {
        font-size: 1.3rem;
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 40px;
        animation: blink 1.5s infinite alternate;
    }
    
    @keyframes blink {
        0% { opacity: 1; }
        100% { opacity: 0.4; }
    }
    
    /* 과목 상자: 장난감 상자 같은 둥근 테두리에 핏자국 포인트 */
    .toy-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 30px;
        border: 4px dashed #ff6b81;
        box-shadow: 5px 5px 0px #2c3e50;
        text-align: center;
        margin-bottom: 15px;
    }
    
    .toy-box h3 {
        margin: 0;
        color: #2f3542;
        font-size: 1.6rem;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 화면 타이틀 렌더링
st.markdown("<div class='creepy-title'>🧸 쉿... 수행평가 알림이 🩸</div>", unsafe_allow_html=True)
st.markdown("<div class='creepy-sub'>똑·딱·똑·딱... 기한을 놓치면 무슨 일이 일어날까? 👁️</div>", unsafe_allow_html=True)
st.write("---")

# 정확한 과목 매핑 (요청사항 반영)
# 국어, 영어, 수학 -> 김용준
# 한국사, 정보, 사회 -> 윤희승
# 음악, 미술, 체육 -> 박현욱
# 나머지 (과학, 과학 탐구, 기가) -> 이현우
subject_mapping = {
    "국어": "pages/김용준.py",
    "영어": "pages/김용준.py",
    "수학": "pages/김용준.py",
    "한국사": "pages/윤희승.py",
    "정보": "pages/윤희승.py",
    "사회": "pages/윤희승.py",
    "음악": "pages/박현욱.py",
    "미술": "pages/박현욱.py",
    "체육": "pages/박현욱.py",
    "과학": "pages/이현우.py",
    "과학 탐구": "pages/이현우.py",
    "기가": "pages/이현우.py",
}

# 12개 과목을 4열 장난감 블록 레이아웃으로 배치
subjects = list(subject_mapping.keys())
cols = st.columns(4)

# 기괴하고 귀여운 이모지 매칭
emojis = ["🎈", "🧸", "🍭", "🎪", "🍼", "🎨", "🚀", "🦖", "🐇", "🔮", "🎭", "🧩"]

for idx, subject in enumerate(subjects):
    with cols[idx % 4]:
        st.markdown(f"""
            <div class='toy-box'>
                <h3>{emojis[idx]} {subject}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        target_page = subject_mapping[subject]
        # 유아틱한 버튼 문구
        if st.button(f"👉 {subject} 보러가기이!", key=f"btn_{subject}", use_container_width=True):
            st.switch_page(target_page)
