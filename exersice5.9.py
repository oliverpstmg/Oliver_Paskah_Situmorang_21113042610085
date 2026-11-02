nama_pengguna = []

if nama_pengguna:
    for pengguna in nama_pengguna:
        if pengguna == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {pengguna.title()}, terima kasih telah masuk kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")