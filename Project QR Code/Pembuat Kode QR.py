import qrcode

data = input("Masukkan teks atau tautan (link): ").strip()
nama_file = input("Masukkan nama file (contoh: qrcode.png): ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
gambar_qr = qr.make_image(fill_color="black", back_color="white")
gambar_qr.save(nama_file)
print(f"✅ QR Code berhasil disimpan dengan nama: {nama_file}")