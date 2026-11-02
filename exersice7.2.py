# Meminta input jumlah orang dan mengonversinya ke tipe integer
group_size = input("Berapa banyak orang dalam rombongan makan malam Anda? ")
group_size = int(group_size)

# Pengondisian berdasarkan jumlah orang
if group_size > 8:
    print("Maaf, Anda harus menunggu meja kosong terlebih dahulu.")
else:
    print("Meja Anda sudah siap! Silakan masuk.")