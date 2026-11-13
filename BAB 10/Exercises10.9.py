filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(f"--- Isi {filename} ---")
            print(contents)
    except FileNotFoundError:
        pass  # Gagal secara senyap tanpa menampilkan pesan error apa pun