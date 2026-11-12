class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

# Membuat beberapa instance yang merepresentasikan pengguna berbeda
user1 = User("Alice", "Smith", "asmith92", "alice@example.com", "New York")
user2 = User("Bob", "Jones", "b_jones", "bob@example.com", "Chicago")
user3 = User("Charlie", "Brown", "charlieb", "charlie@example.com", "Seattle")

# Memanggil kedua method untuk setiap pengguna
users = [user1, user2, user3]
for user in users:
    user.describe_user()
    user.greet_user()