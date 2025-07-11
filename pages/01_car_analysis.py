import streamlit as st
import pandas as pd


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
    st.caption("© 2025 GRIN")

# ────────────────────────────────────────────────────────────────
# Global CSS (Jua font + 카드 개선 + 이미지 아이콘)
# ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    html, body, [class*="css"] { font-family:'Jua', sans-serif; }

    /* Gradient background */
    .stApp {
        background: radial-gradient(circle at 15% 25%, rgba(0,195,120,0.18) 0%, rgba(0,195,120,0) 45%),
                    radial-gradient(circle at 80% 10%, rgba(0,153,255,0.15) 0%, rgba(0,153,255,0) 50%),
                    linear-gradient(130deg, #e9fbff 0%, #ffffff 65%);
    }

    /* Hero gradient text */
    .hero span {
        background: linear-gradient(60deg, #00c378, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ─── Navigation card ─── */
    .card-link {
        display:block;
        border-radius:18px;
        padding:26px 20px;
        height:150px;
        text-decoration:none;          /* 밑줄 제거 */
        color:#e8f2ff;
        background:#ffffff;
        box-shadow:0 4px 16px rgba(0,0,0,0.08);
        transition:transform .25s, box-shadow .25s;
        text-align:center;
    }
    .card-link:hover {
        transform:translateY(-6px);
        box-shadow:0 8px 22px rgba(0,0,0,0.12);
    }
    .card-img { width:56px; margin-bottom:8px; }
    .card-title {
        font-size:22px;                /* 더 큼 */
        margin:0;
        color:#f6f9ff;                 /* 연한 글자색 */
    }

    /* Hide default menu/footer */
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
<h1 class="hero" style="text-align:center; margin-bottom:0.3rem;">
    🐸 <span>GRIN</span> – Green&nbsp;+&nbsp;Information
</h1>
<p style="text-align:center; font-size:20px; color:#547; margin-top:0;">
    보조금·등록 현황, 충전 인프라, 기업&nbsp;FAQ를 한곳에서!
</p>
""",
    unsafe_allow_html=True,
)

st.subheader("원하는 서비스를 선택하세요", divider="rainbow")




col1, col2 = st.columns(2)

with col1:
    button1 = st.button('하나씩 보기')

with col2:
    button2 = st.button('비교해서 보기')


if 'button1' not in st.session_state or 'button2' not in st.session_state:
    st.session_state.button1 = False
    st.session_state.button2 = False

if button1:
    st.session_state.button2=False
    st.session_state.option=''
if button2:
    st.session_state.button1=False
    st.session_state.option=''

chart_list ={
    '연도별 지역별 수소차 보조금': 'C:\skn_17\git\test\project_streamlit\streamlit_files\images\hd_subsidy_heatmap.png',
    '연도별 지역별 전기차 보조금': 'C:\skn_17\git\test\project_streamlit\streamlit_files\images\ev_subsidy_heatmap.png',
    '연도별 전기차와 내연기관차 등록대수현황':'C:\skn_17\git\test\project_streamlit\streamlit_files\images\car & eco cars linegraph.png',
    '연도별 지역별 친환경차 등록대수현황':'C:\skn_17\git\test\project_streamlit\streamlit_files\images\ev_cars_heatmap.png',
    '연도별 지역별 전기차 등록대수현황':'',
    '연도별 지역별 수소차 등록대수현황':''
    }

if button1:
    option = st.selectbox('볼 정보를 선택하세요', chart_list.keys())

    if st.session_state.option !='':
        st.image(chart_list[option],caption=option)
    

