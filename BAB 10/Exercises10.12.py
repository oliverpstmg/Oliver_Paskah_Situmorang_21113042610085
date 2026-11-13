import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Berapa angka favorit Anda? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print("Terima kasih! Angka favorit Anda telah disimpan.")
else:
    print(f"Saya tahu angka favorit Anda! Angkanya adalah {favorite_number}.")