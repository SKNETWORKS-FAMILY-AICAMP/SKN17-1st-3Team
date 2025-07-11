from dict_making import faq_dict as faq_dict
import streamlit as st

# ────────────────────────────────────────────────────────────────
# 기본 설정 & 글로벌 스타일
# ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🐸GRIN🐸 FAQ",
    page_icon="🐸",
    layout="wide",
)

# ────────────────────────────────────────────────────────────────
# 사이드바 – 프로젝트 설명·네비게이션
# ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://img.icons8.com/external-kmg-design-flat-kmg-design/96/228be6/external-electric-car-ecology-kmg-design-flat-kmg-design.png",
        width=70,
    )
    st.markdown(
        """
        ## GRIN🐸  

        전기차 보급을 위한  
        **데이터·인사이트 허브**

        ---

        **주요 메뉴**  
        - 📊 _main_  
        - 🗺️ _car analysis_  
        - 💬 _FAQ_
        """,
    )
    st.markdown("---")
    st.caption("© 2025 GRIN. All rights reserved.")

# ────────────────────────────────────────────────────────────────
# 타이틀 & 서브타이틀
# ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* 구글 폰트 */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    /* 배경 그라데이션 */
    .stApp {
        background: radial-gradient(circle at top left, #d4f5ff 0%, #ffffff 40%, #fefefe 100%);
    }

    /* 헤더 그라데이션 글자 */
    .hero-title span {
        background: linear-gradient(60deg, #00c378, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 선택 카드 */
    .select-card {
        background:#ffffff;
        border-radius:16px;
        padding:1.8rem 1.6rem 2rem;
        box-shadow:0 4px 14px rgba(0,0,0,0.08);
    }

    /* 답변 카드 */
    .answer-card {
        background:#f0f9ff;
        border-left:6px solid #0099ff;
        padding:1.4rem 1.6rem;
        border-radius:14px;
        font-size:17px;
        line-height:1.55;
        color:#003350;
        box-shadow:0 3px 10px rgba(0,0,0,0.08);
        animation:fadeIn 0.5s ease-out;
        transition:transform .2s;
    }
    .answer-card:hover {transform:translateY(-3px);}
    @keyframes fadeIn {from{opacity:0; transform:translateY(8px);} to{opacity:1;transform:none;}}

    /* 위젯 글꼴 */
    div[data-baseweb="select"] *, div[data-baseweb="radio"] label {
        font-size:18px !important;
    }
    div[data-baseweb="select"] div[role="combobox"]{min-height:54px !important;}
    div[data-baseweb="select"],div[data-baseweb="radio"]{width:100% !important;}

    /* 메뉴/푸터 숨김 */
    #MainMenu, footer {visibility:hidden;}
    </style>

    <h1 class="hero-title" style="text-align:center; margin-bottom:0.3rem;">
        🐸<span>GRIN</span>🐸 – Green&nbsp;+&nbsp;Information
    </h1>
    <h4 style="text-align:center; color:#444; margin-top:0;">
        🚘 브랜드별 전기차&nbsp;FAQ
    </h4>
    """,
    unsafe_allow_html=True,
)


# ────────────────────────────────────────────────────────────────
# 두 컬럼 레이아웃
# ────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([3,5], gap="large")

with col_left:
    st.subheader("🛠️ 선택")
    brand = st.radio("브랜드", ['기아','쉐보레','BMW','폴스타'], index=0, horizontal=False)
    match brand:
        case "기아":
            question= st.selectbox("질문",list(faq_dict["질문내용"][0:6]))
        case "쉐보레":
            question= st.selectbox("질문",list(faq_dict["질문내용"][6:16]))
        case "BMW":
            question= st.selectbox("질문",list(faq_dict["질문내용"][16:23]))
        case "폴스타":
            question= st.selectbox("질문",list(faq_dict["질문내용"][-3:]))

                            
index_num=faq_dict['질문내용'].index(question)

with col_right:
    st.subheader("💡 답변")
    st.markdown(f"##### **{brand}** · {question}")
    st.markdown(
        f"<div class='answer-card'>{faq_dict['답변내용'][index_num]}</div>",
        unsafe_allow_html=True,
    )