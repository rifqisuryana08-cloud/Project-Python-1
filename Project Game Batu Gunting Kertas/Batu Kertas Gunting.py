import random

pilihan = ["batu", "kertas", "gunting"]

print("✊✋✌️ GAME BATU GUNTING KERTAS ✊✋✌️")

while True:
    pemain = input("\n👉 Pilih batu, kertas, atau gunting: ").lower()

    if pemain not in pilihan:
        print("⚠️ Pilihan tidak valid! Coba lagi.")
        continue

    komputer = random.choice(pilihan)
    print(f"💻 Komputer memilih: {komputer}")

    if pemain == komputer:
        print("🤝 Hasil seri!")
    elif (
        (pemain == "batu" and komputer == "gunting") or
        (pemain == "kertas" and komputer == "batu") or
        (pemain == "gunting" and komputer == "kertas")
    ):
        print("🎉 Selamat, kamu MENANG!")
    else:
        print("🗿 Kamu KALAH!")

    main_lagi = input("\n🔁 Mau bermain lagi? (y/n): ").lower()
    if main_lagi != "y":
        print("🫰🏼 Terima kasih sudah bermain!")
        break
