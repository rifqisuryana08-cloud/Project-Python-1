Program Game Batu Gunting Kertas ini merupakan versi refactoring dari game sederhana Python yang telah disusun menggunakan function (def). Tujuan refactoring adalah membuat kode lebih rapi, terstruktur, mudah dipahami, dan mudah dikembangkan.
=======================================================================================
✨ Fitur Utama
🎮 Permainan batu–gunting–kertas melawan komputer
🤖 Pilihan komputer dihasilkan secara acak
🔁 Bisa dimainkan berulang kali
⚠️ Validasi input agar tidak terjadi kesalahan
🧩 Kode terstruktur menggunakan function (def)
😊 Tampilan interaktif dengan emoji
=======================================================================================
🛠️ Persyaratan
Python 3.x
Library random (library bawaan Python)
=======================================================================================
▶️ Cara Menjalankan Program
Buka terminal atau command prompt
Masuk ke folder tempat file berada
Jalankan perintah berikut:
python Project Pemfaktoran Ulang Bantu Gunting Kertas.py

Opsi Lain:
Klik Tombol Run jika terdapat tombol run seperti di aplikasi Visual Studio Code atau Python
=======================================================================================
🧠 Penjelasan Struktur Function
tampil_judul()
-> Menampilkan judul permainan di awal program.

input_pemain()
-> Mengambil input dari pemain
-> Memvalidasi input agar hanya menerima batu, gunting, atau kertas

pilihan_komputer()
-> Menghasilkan pilihan komputer secara acak menggunakan random.choice().

tentukan_hasil(pemain, komputer)
-> Menentukan hasil permainan berdasarkan aturan batu–gunting–kertas:
1. Seri
2. Menang
3. Kalah

main()
-> Mengatur alur utama permainan:
1. Menjalankan game
2. Mengulang permainan
3. Mengakhiri game
=======================================================================================
🎮 Cara Bermain
Jalankan program
Masukkan pilihan:
1. batu
2. gunting
3. kertas
Komputer akan memilih secara acak
Hasil permainan akan ditampilkan
Pilih apakah ingin bermain lagi atau keluar
========================================================================================
🧪 Contoh Output
✊✋✌️ GAME BATU GUNTING KERTAS ✊✋✌️

👉 Pilih batu, kertas, atau gunting: batu
💻 Komputer memilih: gunting
🎉 Selamat, kamu MENANG!

🔁 Mau bermain lagi? (y/n): n
🫰🏼 Terima kasih sudah bermain!
=========================================================================================
📚 Konsep Python yang Digunakan
Function (def)
List (list)
Perulangan (while)
Percabangan (if / elif / else)
Validasi input
Library random

