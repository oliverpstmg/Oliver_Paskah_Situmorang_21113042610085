import json

favorite_number = input("Berapa angka favorit Anda? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    
print("Angka favorit Anda telah disimpan!")