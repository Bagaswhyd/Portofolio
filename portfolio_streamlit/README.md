# Portofolio (Streamlit)

Struktur:
  app.py            -> aplikasi Streamlit
  portfolio.html    -> halaman portofolio (edit teks/data di sini)
  static/           -> gambar (about, certs, projects); dibaca app.py lalu ditanam ke halaman
  .streamlit/config.toml -> tema (opsional)
  requirements.txt

Jalankan lokal:
  pip install -r requirements.txt
  streamlit run app.py

Deploy gratis:
  1. Upload seluruh folder ini ke repo GitHub (yang wajib: app.py, portfolio.html, requirements.txt, folder static/).
  2. Buka share.streamlit.io, pilih repo, main file: app.py
  3. Deploy, lalu bagikan link *.streamlit.app

Catatan: setelah mengubah gambar/teks, commit ulang; Streamlit akan memuat ulang.
