class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sekarang sudah buka!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Es Krim'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanila', 'Cokelat', 'Stroberi', 'Mangga', 'Matcha']

    def display_flavors(self):
        print(f"\nDaftar rasa es krim yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Membuat instance dari IceCreamStand dan memanggil method-nya
my_ice_cream_stand = IceCreamStand("Gelato Paradise")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()