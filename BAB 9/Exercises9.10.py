# File Utama: my_restaurant.py

from restaurant import Restaurant

# Membuat instance dari class Restaurant yang diimpor
my_restaurant = Restaurant("Sederhana", "Masakan Padang")

# Memanggil method untuk membuktikan bahwa impor berfungsi dengan baik
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()