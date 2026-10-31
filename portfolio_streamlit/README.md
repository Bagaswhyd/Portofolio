# Portofolio (Streamlit)

Struktur:
  app.py            -> aplikasi Streamlit
  portfolio.html    -> halaman portofolio (edit teks/data di sini)
  static/           -> gambar (about, certs, projects)
  .streamlit/config.toml -> mengaktifkan static serving
  requirements.txt

Jalankan lokal:
  pip install -r requirements.txt
  streamlit run app.py

Deploy gratis:
  1. Upload seluruh folder ini ke repo GitHub (termasuk .streamlit/ dan static/).
  2. Buka share.streamlit.io, pilih repo, main file: app.py
  3. Deploy, lalu bagikan link *.streamlit.app

Catatan: setelah mengubah gambar/teks, commit ulang; Streamlit akan memuat ulang.
