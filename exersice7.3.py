# Meminta input angka
number = input("Masukkan sebuah angka: ")
number = int(number)

# Memeriksa apakah angka merupakan kelipatan 10
if number % 10 == 0:
    print(f"Angka {number} adalah kelipatan 10.")
else:
    print(f"Angka {number} BUKAN kelipatan 10.")        