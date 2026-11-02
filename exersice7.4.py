prompt = "\nMasukkan topping pizza yang Anda inginkan:"
prompt += "\n(Ketik 'quit' jika sudah selesai): "

while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")