pengguna_lama = ['admin', 'budi', 'siti', 'ani', 'eko']
pengguna_baru = ['Budi', 'joko', 'SITI', 'riki', 'dewi']

# Membuat list baru dengan versi huruf kecil semua untuk perbandingan
pengguna_lama_kecil = [pengguna.lower() for pengguna in pengguna_lama]

for p_baru in pengguna_baru:
    if p_baru.lower() in pengguna_lama_kecil:
        print(f"Maaf, nama pengguna '{p_baru}' sudah digunakan. Anda harus memasukkan nama pengguna baru.")
    else:
        print(f"Nama pengguna '{p_baru}' tersedia.")