def describe_city(city, country='Indonesia'):
    """Menampilkan deskripsi kota dan negaranya."""
    print(f"{city} berada di {country}.")

# Memanggil fungsi untuk tiga kota berbeda
describe_city('Surakarta')           # Menggunakan negara default
describe_city('Bandung')             # Menggunakan negara default
describe_city('Tokyo', 'Jepang')     # Menggunakan negara non-default