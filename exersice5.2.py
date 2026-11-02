# 1. Tes kesetaraan dan ketidaksetaraan string
nama = 'Budi'
print(nama == 'Budi')  # True
print(nama != 'Andi')  # True

# 2. Tes menggunakan metode lower()
kota = 'Surabaya'
print(kota.lower() == 'surabaya')  # True

# 3. Tes numerik (kesetaraan, ketidaksetaraan, perbandingan ukuran)
usia = 21
print(usia == 21)  # True
print(usia != 18)  # True
print(usia > 17)   # True
print(usia < 25)   # True
print(usia >= 21)  # True
print(usia <= 20)  # False

# 4. Tes menggunakan operator and dan or
print((usia > 18) and (kota == 'Surabaya'))  # True
print((usia < 15) or (kota == 'Surabaya'))   # True

# 5. Tes keanggotaan item dalam list (in / not in)
material = ['baja', 'besi', 'aluminium']
print('baja' in material)        # True
print('tembaga' not in material) # True
