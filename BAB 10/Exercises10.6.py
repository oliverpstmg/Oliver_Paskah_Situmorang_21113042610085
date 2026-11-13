print("Masukkan dua angka untuk dijumlahkan.")

try:
    first_number = input("Masukkan angka pertama: ")
    num1 = int(first_number)
    
    second_number = input("Masukkan angka kedua: ")
    num2 = int(second_number)
except ValueError:
    print("Kesalahan: Harap masukkan angka yang valid, bukan teks!")
else:
    sum_result = num1 + num2
    print(f"Hasil penjumlahan: {num1} + {num2} = {sum_result}")