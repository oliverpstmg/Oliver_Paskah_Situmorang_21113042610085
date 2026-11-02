def make_shirt(size='large', text='I love Python'):
    """Membuat kaos dengan nilai default ukuran L dan teks 'I love Python'."""
    print(f"Membuat kaos ukuran {size.title()} dengan teks: '{text}'.")

# 1. Kaos besar dengan pesan default
make_shirt()

# 2. Kaos sedang dengan pesan default
make_shirt(size='medium')

# 3. Kaos ukuran apa saja (misal: S) dengan pesan berbeda
make_shirt(size='small', text='Belajar Algoritma')