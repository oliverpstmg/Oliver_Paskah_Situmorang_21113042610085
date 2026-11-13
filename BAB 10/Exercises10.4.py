filename = 'guest.txt'

# Meminta input nama dari pengguna
name = input("Masukkan nama Anda: ")

# Menulis nama ke dalam file guest.txt
with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Terima kasih, {name}! Nama Anda telah disimpan ke dalam file {filename}.")