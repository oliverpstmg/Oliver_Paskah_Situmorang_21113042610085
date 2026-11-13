filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

# Langsung melakukan perulangan pada contents.splitlines() tanpa variabel sementara
print("--- Kode lebih ringkas tanpa variabel sementara ---")
for line in contents.splitlines():
    print(line)