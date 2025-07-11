import streamlit as st

# ────────────────────────────────────────────────────────────────
# Page configuration
# ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🐸GRIN🐸 – Home",
    page_icon="🐸",
    layout="wide",
)

# ────────────────────────────────────────────────────────────────
# Sidebar – brief project intro
# ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://img.icons8.com/external-kmg-design-flat-kmg-design/96/6dce9e/external-electric-car-ecology-kmg-design-flat-kmg-design.png",
        width=80,
    )
    st.subheader("🐸 GRIN – Green + Information")
    st.caption("전기차 보급을 위한 데이터·인사이트 허브")
    st.markdown("---")
    st.caption("© 2025 GRIN. All rights reserved")

# ────────────────────────────────────────────────────────────────
# Global CSS (Jua + 카드·이미지 크기)
# ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    html, body, [class*="css"] { font-family:'Jua', sans-serif; }

    /* Background */
    .stApp {
        background: radial-gradient(circle at 15% 25%, rgba(0,195,120,0.18) 0%, rgba(0,195,120,0) 45%),
                    radial-gradient(circle at 80% 10%, rgba(0,153,255,0.15) 0%, rgba(0,153,255,0) 50%),
                    linear-gradient(130deg, #e9fbff 0%, #ffffff 65%);
    }

    /* Hero gradient */
    .hero span {
        background: linear-gradient(60deg, #00c378, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Navigation card */
    .card-link {
        display:block;
        border-radius:18px;
        padding:24px 18px 22px;
        height:140px;
        text-decoration:none;      /* no underline */
        color:#003350;
        background:#ffffff;
        box-shadow:0 4px 16px rgba(0,0,0,0.08);
        transition:transform .25s, box-shadow .25s;
        text-align:center;
    }
    .card-link:hover {
        transform:translateY(-6px);
        box-shadow:0 8px 22px rgba(0,0,0,0.12);
    }

    /* 아이콘 이미지 크기 축소 */
    .card-img { width:48px; margin-bottom:8px; }

    .card-title{
        font-size:18px;
        font-weight:600;
        margin:0;
        font-family:'Jua', sans-serif;
    }

    #MainMenu, footer {visibility:hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ────────────────────────────────────────────────────────────────
# Hero section
# ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <h1 class="hero" style="text-align:center; margin-bottom:0.25em;">
        🐸 <span>GRIN</span> – Green&nbsp;+&nbsp;Information
    </h1>
    <p style="text-align:center; font-size:18px; color:#444; margin-top:0;">
        보조금·등록 현황, 충전 인프라, 기업&nbsp;FAQ를 한곳에서!
    </p>
    """,
    unsafe_allow_html=True,
)

st.subheader("원하는 서비스를 선택하세요", divider="rainbow")

# ────────────────────────────────────────────────────────────────
# Navigation cards (2 × 2 grid) with small image icons
# ────────────────────────────────────────────────────────────────
row1_col1, row1_col2 = st.columns(2, gap="large")
row2_col1, row2_col2 = st.columns(2, gap="large")

cards = [
    ("http://localhost:8501/car_analysis",
     "https://img.icons8.com/fluency/96/combo-chart.png",
     "전국 보급 대시보드"),
    
    ("http://localhost:8501/faq",
     "https://img.icons8.com/fluency/96/faq.png",
     "기업 FAQ 조회"),
]

cols = [row1_col1, row1_col2,]
for col, (link, img_url, title) in zip(cols, cards):
    col.markdown(
        f"""
        <a href="{link}" class="card-link">
            <img src="{img_url}" class="card-img">
            <p class="card-title">{title}</p>
        </a>
        """,
        unsafe_allow_html=True,
    )