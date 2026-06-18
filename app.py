  import streamlit as st

# 1. 페이지 기본 설정 (에러 방지를 위해 가장 최상단에 배치)
st.set_page_config(
    page_title="🧸 쉿! 수행평가 알림이 🩸",
    page_icon="🤡",
    layout="wide"
)

# 2. [유아틱 + 소름돋는] 잔혹동화풍 Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdee9 0%, #b5fffc 100%);
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
    }
    .creepy-title {
        font-size: 3.5rem !important;
        font-weight: 900;
        color: #ff4757;
        text-align: center;
        text-shadow: 3px 3px 0px #000000, 5px 5px 10px rgba(255, 0, 0, 0.5);
        margin-top: 20px;
        margin-bottom: 5px;
    }
    .creepy-sub {
        font-size: 1.3rem;
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 40px;
    }
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

# 메인 화면 타이틀
st.markdown("<div class='creepy-title'>🧸 쉿... 수행평가 알림이 🩸</div>", unsafe_allow_html=True)
st.markdown("<div class='creepy-sub'>똑·딱·똑·딱... 기한을 놓치면 무슨 일이 일어날까? 👁️</div>", unsafe_allow_html=True)
st.write("---")

# 3. 과목 및 파일 매핑 (경로 에러 방지를 위해 pages/ 빼고 파일명만 매핑)
subject_mapping = {
    "국어": "김용준.py",
    "영어": "김용준.py",
    "수학": "김용준.py",
    "한국사": "윤희승.py",
    "정보": "윤희승.py",
    "사회": "윤희승.py",
    "음악": "박현욱.py",
    "미술": "박현욱.py",
    "체육": "박현욱.py",
    "과학": "이현우.py",
    "과학 탐구": "이현우.py",
    "기가": "이현우.py",
}

# 12개 과목 배치
subjects = list(subject_mapping.keys())
cols = st.columns(4)
emojis = ["🎈", "🧸", "🍭", "🎪", "🍼", "🎨", "🚀", "🦖", "🐇", "🔮", "🎭", "🧩"]

for idx, subject in enumerate(subjects):
    with cols[idx % 4]:
        st.markdown(f"""
            <div class='toy-box'>
                <h3>{emojis[idx]} {subject}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        filename = subject_mapping[subject]
        
        # 버튼을 누르면 안전하게 pages/파일명.py 구조로 전환되도록 설정
        if st.button(f"👉 {subject} 보러가기이!", key=f"btn_{subject}", use_container_width=True):
            try:
                st.switch_page(f"pages/{filename}")
            except Exception as e:
                st.error(f"⚠️ '{filename}' 파일을 찾을 수 없어! GitHub에 pages 폴더와 파일이 올바르게 있는지 확인해줘.")
