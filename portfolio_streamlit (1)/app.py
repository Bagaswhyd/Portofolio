"""Portofolio Muhammad Bagas Wahyudi - dibungkus di Streamlit.

Tampilan, animasi, dan pilihan bahasa ID/EN berasal dari portfolio.html.
Semua gambar di folder ./static dimasukkan langsung ke halaman (base64),
jadi tidak perlu pengaturan static serving atau folder tersembunyi.
"""
import base64
import json
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

# Dipasang sebelum skrip portofolio: mengganti setiap <img src="projects/..."> dkk
# dengan data URI yang sesuai (termasuk gambar yang dibuat dinamis oleh JavaScript).
BOOT = """
<script>
window.ASSETS = __ASSETS__;
(function () {
  function fix(img) {
    var s = img.getAttribute('src');
    if (s && window.ASSETS[s]) img.setAttribute('src', window.ASSETS[s]);
  }
  new MutationObserver(function (muts) {
    muts.forEach(function (m) {
      if (m.type === 'attributes') { fix(m.target); return; }
      m.addedNodes.forEach(function (n) {
        if (n.nodeType !== 1) return;
        if (n.tagName === 'IMG') fix(n);
        n.querySelectorAll && n.querySelectorAll('img').forEach(fix);
      });
    });
  }).observe(document, {childList: true, subtree: true, attributes: true, attributeFilter: ['src']});
})();
</script>
<style>.lb-bar a{display:none !important;}</style>
"""


@st.cache_data(show_spinner="Memuat portofolio...")
def build_html() -> str:
    assets = {}
    for p in sorted((BASE / "static").rglob("*.jpg")):
        rel = p.relative_to(BASE / "static").as_posix()  # mis. projects/thumb/x.jpg
        assets[rel] = "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
    boot = BOOT.replace("__ASSETS__", json.dumps(assets).replace("</", "<\\/"))
    html = (BASE / "portfolio.html").read_text(encoding="utf-8")
    return html.replace("<head>", "<head>" + boot, 1)


components.html(build_html(), height=1000, scrolling=True)
