# Project Python 1
# Replikasi dan Dokumentasi
Repository ini berisi **kumpulan mini game Python sederhana** yang dibuat sebagai latihan dasar pemrograman Python. Setiap game dirancang interaktif, mudah dipahami, dan cocok untuk pemula. Seluruh program menggunakan bahasa Indonesia dan sebagian telah direfaktor menggunakan **function (`def`)** agar kodenya lebih rapi dan terstruktur.

---

## 📌 Daftar Game

1. 🎲 Game Dadu
2. 🎯 Game Tebak Angka
3. ✊✋✌️ Game Batu Gunting Kertas
4. ✊✋✌️ Game Batu Gunting Kertas (Versi Refactoring dengan Function)
5. 🔲 QR Code Generator

---

## 🛠️ Persyaratan Umum

* Python **3.x**
* Library bawaan Python:

  * `random`
* Library tambahan (khusus QR Code Generator):

  * `qrcode`

Instalasi library QR Code:

```bash
pip install qrcode[pil]
```

---

## 📂 Struktur Folder (Contoh)

```
project-folder/
│
├── game_dadu.py
├── game_tebak_angka.py
├── game_batu_gunting_kertas.py
├── game_batu_gunting_kertas_refactor.py
├── qr_code_generator.py
└── README.md
```

---

## 🎲 1. Game Dadu

### Deskripsi

Game ini mensimulasikan lemparan dadu dengan hasil angka **1–6**. Pemain dapat memilih untuk melempar dadu atau keluar dari permainan.

### Fitur

* Lempar dadu secara acak
* Bermain berulang kali
* Input sederhana (y/n)

### Konsep Python

* `while loop`
* `if / elif / else`
* `random.randint()`

---

## 🎯 2. Game Tebak Angka

### Deskripsi

Pemain diminta menebak angka rahasia dari **1 sampai 10** yang diacak oleh komputer. Program akan memberi petunjuk dan menghitung jumlah percobaan.

### Fitur

* Angka acak setiap permainan
* Petunjuk terlalu besar / kecil
* Perhitungan jumlah percobaan
* Opsi bermain ulang

### Konsep Python

* Perulangan bersarang (`while`)
* Input & output
* Percabangan
* `random.randint()`

---

## ✊✋✌️ 3. Game Batu Gunting Kertas

### Deskripsi

Permainan klasik batu–gunting–kertas antara pemain dan komputer dengan validasi input.

### Fitur

* Pilihan komputer acak
* Validasi input
* Bermain ulang

### Konsep Python

* List (`list`)
* Percabangan logika
* Perulangan

---

## ✊✋✌️ 4. Game Batu Gunting Kertas (Refactoring)

### Deskripsi

Versi pengembangan dari game batu gunting kertas yang telah **direfaktor menggunakan function (`def`)** agar kode lebih terstruktur dan mudah dikembangkan.

### Fitur Tambahan

* Struktur kode modular
* Function terpisah untuk setiap tugas
* Lebih mudah dikembangkan

### Function Utama

* `tampil_judul()`
* `input_pemain()`
* `pilihan_komputer()`
* `tentukan_hasil()`
* `main()`

### Konsep Python

* Function (`def`)
* Modular programming
* Best practice Python dasar

---

## 🔲 5. QR Code Generator

### Deskripsi

Program ini digunakan untuk membuat **QR Code** dari teks atau link yang dimasukkan oleh pengguna dan menyimpannya sebagai file gambar.

### Fitur

* Input teks atau URL
* Nama file bebas
* Output berupa gambar QR Code

### Konsep Python

* Input pengguna
* Library eksternal `qrcode`
* Manipulasi file




---

## 📄 Lisensi

Bebas digunakan untuk pembelajaran, tugas sekolah/kuliah, dan pengembangan pribadi.
