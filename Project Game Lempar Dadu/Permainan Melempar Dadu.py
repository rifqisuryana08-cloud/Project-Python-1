import random

print("🎲 GAME DADU 🎲")
print("Ketik 'y' untuk melempar dadu, 'n' untuk keluar.")

while True:
    pilihan = input("\nPilihan kamu (y/n): ").lower()

    if pilihan == "y":
        print("🎲 Dadu sedang dilempar...")
        dadu = random.randint(1, 6)
        print(f"🔥 Hasilnya adalah: {dadu}")
    elif pilihan == "n":
        print("🎲 Keluar dari permainan. Terima kasih!")
        break
    else:
        print("❓Pilihan tidak dikenal, coba lagi.")


