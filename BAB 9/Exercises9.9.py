class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        print(f"Mobil ini dapat menempuh jarak sekitar {range_miles} mil dengan baterai penuh.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai telah ditingkatkan menjadi 65-kWh.")
        else:
            print("Baterai sudah berkapasitas penuh.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# Membuat mobil listrik, memeriksa jangkauan awal, meningkatkan baterai, dan memeriksa ulang
my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("\nMemutakhirkan baterai...")
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()