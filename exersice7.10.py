responses = {}

# Menandai bahwa jajak pendapat sedang aktif
polling_active = True

while polling_active:
    # Meminta nama dan jawaban responden
    name = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    
    # Menyimpan jawaban ke dalam kamus (dictionary)
    responses[name] = response
    
    # Menanyakan apakah ada orang lain yang ingin mengisi jajak pendapat
    repeat = input("Apakah ada orang lain yang ingin mengisi jajak pendapat? (ya/tidak): ")
    if repeat.lower() == 'tidak':
        polling_active = False

# Jajak pendapat selesai, tampilkan hasil
print("\n--- Hasil Jajak Pendapat Liburan Impian ---")
for name, place in responses.items():
    print(f"{name.title()} ingin mengunjungi {place.title()}.")