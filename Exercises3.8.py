places =["Swis","Amerika Serikat","Jerman","Jepang","China","Belanda"]

# 1. Cetak urutan asli
print("Urutan asli:", places)

# 2. Urutan alfabet menggunakan sorted() (sementara)
print("Urutan sorted():", sorted(places))

# 3. Buktikan list asli tidak berubah
print("Urutan asli setelah sorted():", places)

# 4. Urutan alfabet terbalik menggunakan sorted(..., reverse=True)
print("Urutan alfabet terbalik (sorted):", sorted(places, reverse=True))

# 5. Buktikan list asli tetap tidak berubah

print("Urutan asli setelah sorted reverse:", places)

# 6. Ubah urutan permanen dengan reverse()
places.reverse()
print("Setelah reverse():", places)

# 7. Kembalikan ke urutan asli dengan reverse() lagi
places.reverse()
print("Dikembalikan ke asli dengan reverse():", places)

# 8. Urutkan secara permanen secara alfabet dengan sort()
places.sort()
print("Setelah sort() alfabet:", places)

# 9. Urutkan secara permanen secara alfabet terbalik dengan sort(reverse=True)
places.sort(reverse=True)
print("Setelah sort() alfabet terbalik:", places)