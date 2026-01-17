import random

print("🎯 GAME TEBAK ANGKA 🎯")
print("Tebak angka dari 1 sampai 10.")

while True:
    angka_rahasia = random.randint(1, 10)
    tebakan = 0
    percobaan = 0

    while tebakan != angka_rahasia:
        tebakan = int(input("\n❓ Masukkan tebakanmu: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("⬆️ Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("⬇️ Terlalu besar!")
        else:
            print(f"🎉 Benar! Angkanya adalah {angka_rahasia}")
            print(f"🏆 Kamu berhasil dalam {percobaan} percobaan")

    main_lagi = input("\n🔁 Mau bermain lagi? (y/n): ").lower()
    if main_lagi != "y":
        print("🫰🏼 Terima kasih sudah bermain!")
        break
