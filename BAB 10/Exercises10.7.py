print("=== Kalkulator Penjumlahan ===")
print("Ketik 'q' kapan saja untuk keluar.\n")

while True:
    first_number = input("Masukkan angka pertama: ")
    if first_number.lower() == 'q':
        break
        
    second_number = input("Masukkan angka kedua: ")
    if second_number.lower() == 'q':
        break
        
    try:
        num1 = int(first_number)
        num2 = int(second_number)
    except ValueError:
        print("Error: Mohon masukkan angka yang valid, bukan huruf atau teks!\n")
    else:
        sum_result = num1 + num2
        print(f"Hasil dari {num1} + {num2} adalah {sum_result}\n")