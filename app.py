import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="고등학교 수행평가 알림이",
    page_icon="📅",
    layout="wide"
)

# 2. 예쁜 배경 및 디자인을 위한 Custom CSS 적용
st.markdown("""
    <style>
    /* 전체 배경색 및 폰트 설정 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* 메인 타이틀 스타일 */
    .main-title {
        font-size: 3rem !important;
        font-weight: 800;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* 서브 타이틀 스타일 */
    .sub-title {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 40px;
    }
    
    /* 과목 카드 스타일 */
    .subject-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* 안내 문구 스타일 */
    .info-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2196f3;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 세션 상태(Session State)를 이용한 페이지 전환 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Main'

# --- 샘플 데이터 ---
subjects_data = {
    "국어": {"date": "2026-07-02", "content": "현대시 분석 및 비평문 작성 (지필 포함)", "status": "🔴 마감 임박"},
    "수학": {"date": "2026-06-25", "content": "미분계수의 기하학적 의미 탐구 보고서 제출", "status": "🟡 진행 중"},
    "과학": {"date": "2026-06-30", "content": "화학 반응 속도 실험 결과 분석 및 보고서", "status": "🟡 진행 중"},
    "과학탐구": {"date": "2026-07-05", "content": "자유 주제 과학 탐구 실험 설계 및 발표", "status": "🟢 여유 있음"},
    "사회": {"date": "2026-06-23", "content": "현대 사회 문제 해결을 위한 조별 PPT 발표", "status": "🔴 마감 임박"},
    "음악": {"date": "2026-07-08", "content": "가창 실기 평가 (지정곡 1곡 택일)", "status": "🟢 여유 있음"},
    "체육": {"date": "2026-06-29", "content": "배드민턴 하이클리어 및 서브 정확도 측정", "status": "🟡 진행 중"},
    "미술": {"date": "2026-07-10", "content": "팝아트 기법을 활용한 자화상 그리기", "status": "🟢 여유 있음"},
    "한국사": {"date": "2026-06-24", "content": "일제강점기 독립운동가 생애 조사 카드뉴스 제작", "status": "🔴 마감 임박"},
    "기가": {"date": "2026-07-03", "content": "주거 공간 설계 및 3D 모델링 구상", "status": "🟢 여유 있음"},
    "정보": {"date": "2026-06-26", "content": "Python을 활용한 정렬 알고리즘 구현 수행", "status": "🟡 진행 중"},
    "영어": {"date": "2026-07-01", "content": "영문 에세이 작성 및 3분 스피치", "status": "🟡 진행 중"},
}

# ==============================================================================
# 4. [페이지 1] 메인 페이지 화면
# ==============================================================================
if st.session_state.current_page == 'Main':
    st.markdown("<div class='main-title'>📅 수행평가 알림이</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>과목을 선택하면 상세 수행평가 일정과 내용을 확인할 수 있습니다.</div>", unsafe_allow_html=True)
    
    subjects = ["국어", "수학", "과학", "과학탐구", "사회", "음악", "체육", "미술", "한국사", "기가", "정보", "영어"]
    
    # 4열 레이아웃 배치
    cols = st.columns(4)
    
    for idx, subject in enumerate(subjects):
        with cols[idx % 4]:
            st.markdown(f"""
                <div class='subject-card'>
                    <h3>📚 {subject}</h3>
                    <p style='color:#7f8c8d; font-size:0.9rem;'>클릭하여 일정 확인</p>
                </div>
            """, unsafe_allow_html=True)
            
            # 버튼 클릭 시 해당 과목 페이지로 이동
            if st.button(f"{subject} 일정 보기", key=f"btn_{subject}", use_container_width=True):
                st.session_state.current_page = subject
                st.rerun()

# ==============================================================================
# 5. [페이지 2] 과목별 상세 페이지 화면
# ==============================================================================
else:
    chosen_sub = st.session_state.current_page
    
    if st.button("⬅️ 메인 화면으로 돌아가기", use_container_width=False):
        st.session_state.current_page = 'Main'
        st.rerun()
        
    st.write("---")
    st.title(f"📚 {chosen_sub} 수행평가 상세 일정")
    
    info = subjects_data.get(chosen_sub, {"date": "미정", "content": "등록된 수행평가 정보가 없습니다.", "status": "🟢 정보 없음"})
    
    st.markdown(f"""
        <div class='info-box'>
            <h4>📌 진행 상태: {info['status']}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="📅 마감일", value=info['date'])
    with col2:
        st.subheader("📝 수행평가 내용")
        st.info(info['content'])
        
    st.warning("⚠️ 수행평가 일정은 학교 사정에 따라 변경될 수 있으니 항상 공지사항을 재확인하세요!")
