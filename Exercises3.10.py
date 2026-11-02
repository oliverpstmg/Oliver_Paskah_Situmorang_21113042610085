# Membuat list negara
countries = ["Swis","Amerika Serikat","Jerman","Jepang","China","Belanda"]
# 1. Mengakses elemen menggunakan indeks
print("Negara pertama:", countries[0])

# 2. Mengubah elemen
countries[2] = "Argentina"
print("Setelah diubah:", countries)

# 3. Menambahkan elemen dengan append()
countries.append("Australia")
print("Setelah append:", countries)

# 4. Menyisipkan elemen dengan insert()
countries.insert(1, "Prancis")
print("Setelah insert:", countries)

# 5. Menghapus elemen dengan del
del countries[5]
print("Setelah del:", countries)

# 6. Menghapus elemen terakhir dengan pop()
popped_country = countries.pop()
print("Negara yang di-pop:", popped_country)
print("Setelah pop:", countries)

# 7. Menghapus elemen berdasarkan nilai dengan remove()
countries.remove("Amerika Serikat")
print("Setelah remove Amerika Serikat:", countries)

# 8. Menggunakan sorted() (sementara)
print("Sorted:", sorted(countries))

# 9. Menggunakan reverse()
countries.reverse()
print("Setelah reverse:", countries)

# 10. Menggunakan sort()
countries.sort()
print("Setelah sort:", countries)

# 11. Menghitung panjang list dengan len()
print("Jumlah negara saat ini:", len(countries))