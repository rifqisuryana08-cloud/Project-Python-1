Program ini adalah aplikasi sederhana berbasis Python untuk membuat QR Code dari teks atau tautan (link).
QR Code yang dihasilkan akan disimpan dalam bentuk file gambar (.png).
======================================================================================
🔤 Input teks atau URL secara bebas
🖼️ Menghasilkan QR Code dalam format gambar
💾 Nama file bisa ditentukan sendiri
⚡ Cepat dan mudah digunakan
🧩 Menggunakan library qrcode
======================================================================================
🛠️ Persyaratan
Pastikan sudah terinstall:
Python 3.10+
Virtual Environment (venv)
======================================================================================
Library yang dibutuhkan:
qrcode[pil]
======================================================================================
📥 Instalasi
1️⃣ Aktifkan Virtual Environment
.\venv\Scripts\Activate.ps1

2️⃣ Install Library qrcode
pip install qrcode[pil]
======================================================================================
▶️ Cara Menjalankan Program
Gunakan Python dari venv (WAJIB):
.\venv\Scripts\python.exe "Pembuat Kode QR.py"
======================================================================================
🧪 Contoh Penggunaan
Saat program dijalankan:
Masukkan teks atau tautan (link): https://google.com
Masukkan nama file (contoh: qrcode.png): google_qr.png
✅ QR Code berhasil disimpan dengan nama: google_qr.png
======================================================================================
⚠️ Catatan Penting
Pastikan menjalankan Python dari virtual environment
Jangan menggunakan Python global jika module tidak terdeteksi
Nama file sebaiknya diakhiri dengan .png bisa juga .jpg


