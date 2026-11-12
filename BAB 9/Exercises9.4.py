class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atribut baru dengan nilai default 0

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")
        print(f"Jumlah Pelanggan yang Dilayani: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sekarang sudah buka!")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang telah dilayani ke nilai tertentu."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Menambahkan jumlah pelanggan yang dilayani dengan angka baru."""
        self.number_served += additional_customers

# Membuat instance bernama restaurant
restaurant = Restaurant("The Golden Spoon", "Italia")

# 1. Mencetak jumlah pelanggan awal
print(f"Jumlah pelanggan awal: {restaurant.number_served}")

# Mengubah nilai secara langsung dan mencetaknya lagi
restaurant.number_served = 15
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

# 2. Menggunakan method set_number_served()
restaurant.set_number_served(50)
print(f"Jumlah pelanggan setelah menggunakan set_number_served(50): {restaurant.number_served}")

# 3. Menggunakan method increment_number_served() (misal: tambahan pelanggan hari ini)
restaurant.increment_number_served(120)
print(f"Jumlah pelanggan setelah increment_number_served(120): {restaurant.number_served}")