import random

PILIHAN = ["batu", "kertas", "gunting"]

def tampil_judul():
    print("✊✋✌️ GAME BATU GUNTING KERTAS ✊✋✌️")

def input_pemain():
    while True:
        pilihan = input("\n👉 Pilih batu, kertas, atau gunting: ").lower()
        if pilihan in PILIHAN:
            return pilihan
        else:
            print("⚠️ Pilihan tidak valid! Coba lagi.")

def pilihan_komputer():
    return random.choice(PILIHAN)

def tentukan_hasil(pemain, komputer):
    if pemain == komputer:
        return "🤝 Hasil seri!"
    elif (
        (pemain == "batu" and komputer == "gunting") or
        (pemain == "kertas" and komputer == "batu") or
        (pemain == "gunting" and komputer == "kertas")
    ):
        return "🎉 Selamat, kamu MENANG!"
    else:
        return "🗿 Kamu KALAH!"

def main():
    tampil_judul()

    while True:
        pemain = input_pemain()
        komputer = pilihan_komputer()

        print(f"💻 Komputer memilih: {komputer}")
        hasil = tentukan_hasil(pemain, komputer)
        print(hasil)

        main_lagi = input("\n🔁 Mau bermain lagi? (y/n): ").lower()
        if main_lagi != "y":
            print("🫰🏼 Terima kasih sudah bermain!")
            break

main()
