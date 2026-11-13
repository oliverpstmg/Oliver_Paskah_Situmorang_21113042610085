import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("Belum ada angka yang disimpan.")
else:
    print(f"Saya tahu angka favorit Anda! Angkanya adalah {favorite_number}.")