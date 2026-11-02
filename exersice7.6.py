topping = ""
while topping.lower() != 'quit':
    topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
    if topping.lower() != 'quit':
        print(f"Menambahkan {topping} ke pizza Anda.")