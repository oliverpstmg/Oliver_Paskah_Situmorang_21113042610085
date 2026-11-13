 filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nMencoba membaca file: {filename}")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak dapat ditemukan.")6
        