filename = 'guest_book.txt'

print("=== BUKU TAMU ===")
print("Ketik 'quit' atau 'selesai' jika sudah selesai memasukkan nama.\n")

# Membuka file dalam mode 'w' (atau 'a' jika ingin menambahkan ke file yang sudah ada)
with open(filename, 'w') as file_object:
    while True:
        name = input("Masukkan nama tamu: ")
        
        # Kondisi untuk menghentikan perulangan
        if name.lower() in ['quit', 'selesai', 'q']:
            print("Pencatatan buku tamu selesai.")
            break
            
        # Menulis nama ke file diikuti dengan karakter baris baru (\n)
        file_object.write(f"{name}\n")
        print(f"Selamat datang, {name}! Kehadiran Anda telah dicatat.")

print(f"\nSemua nama tamu berhasil disimpan ke dalam file {filename}.")