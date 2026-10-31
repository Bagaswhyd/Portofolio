"""Portofolio Muhammad Bagas Wahyudi - dibungkus di Streamlit.

Tampilan, animasi, dan pilihan bahasa ID/EN berasal dari portfolio.html.
Gambar disajikan lewat Streamlit static serving (folder ./static, lihat
.streamlit/config.toml), jadi folder static/ harus ikut di-upload.
"""
import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent

st.set_page_config(
    page_title="Muhammad Bagas Wahyudi - Data Analyst & ML",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hilangkan header/footer/padding Streamlit agar portofolio memenuhi layar.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu {display:none !important;}
      .block-container {padding:0 !important; max-width:100% !important;}
      iframe {height:100vh !important; width:100% !important; border:0;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_html() -> str:
    html = (BASE / "portfolio.html").read_text(encoding="utf-8")
    # Arahkan path gambar relatif ke folder static milik Streamlit.
    # Mengubah  "projects/...", 'certs/...', "about/..."  menjadi /app/static/...
    return re.sub(
        r"""(["'])(projects|certs|about)/""",
        r"\1/app/static/\2/",
        html,
    )


components.html(load_html(), height=1000, scrolling=True)
