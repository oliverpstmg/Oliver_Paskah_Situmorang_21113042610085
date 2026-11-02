while True:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
    if topping.lower() == 'quit':
        break
    print(f"Menambahkan {topping} ke pizza Anda.")