# Visualisasi Interaktif (Streamlit)

Aplikasi demo Streamlit yang menampilkan 5 jenis visualisasi dari dataset contoh 10 baris.

Fitur:
- Dropdown untuk memilih: Pie Chart, Area Chart, Bar Chart, Line Chart, Map
- Tampilan gambar, judul, dan deskripsi
- Tabel data dan tombol unduh CSV

Cara menjalankan:

1. (Optional) buat virtualenv dan aktifkan

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

3. Jalankan Streamlit

```powershell
streamlit run app.py
```

Catatan: file gambar contoh juga tersedia lokal pada `assets/sample_image.svg` — aplikasi akan menampilkan file lokal tersebut jika ditemukan, jika tidak maka akan menampilkan gambar dari internet.

Silakan hubungi saya kalau mau ditambahkan filter, multi-select, atau data nyata.
