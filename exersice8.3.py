def make_shirt(size, text):
    """Merangkum ukuran kaos dan pesan yang dicetak."""
    print(f"Membuat kaos ukuran {size} dengan teks cetak: '{text}'.")

# 1. Memanggil fungsi menggunakan argumen posisional
make_shirt('L', 'Teknik Industri UI')

# 2. Memanggil fungsi menggunakan argumen kata kunci (keyword arguments)
make_shirt(size='M', text='Python Programmer')