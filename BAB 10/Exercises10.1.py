filename = 'learning_python.txt'

# 1. Membaca seluruh file sekaligus
print("--- 1. Membaca seluruh file sekaligus ---")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# 2. Menyimpan baris-baris dalam list dan melakukan looping
print("--- 2. Membaca melalui perulangan pada list baris ---")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())  # .strip() digunakan untuk menghapus baris baru ekstra (\n)
