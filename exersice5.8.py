nama_pengguna = ['admin', 'budi', 'siti', 'ani', 'eko']

for pengguna in nama_pengguna:
    if pengguna == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {pengguna.title()}, terima kasih telah masuk kembali.")