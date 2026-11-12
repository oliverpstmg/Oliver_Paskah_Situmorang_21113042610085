class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Atribut baru dengan nilai default 0

    def describe_user(self):
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.location}")
        print(f"  Percobaan Login: {self.login_attempts}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambahkan nilai login_attempts sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mereset nilai login_attempts kembali menjadi 0."""
        self.login_attempts = 0

# Membuat instance dari User
user = User("Budi", "Santoso", "budisantoso", "budi@example.com", "Jakarta")

# Memanggil increment_login_attempts() beberapa kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Mencetak nilai login_attempts untuk memastikan bertambah dengan benar
print(f"Jumlah percobaan login setelah beberapa kali increment: {user.login_attempts}")

# Memanggil method reset_login_attempts()
user.reset_login_attempts()

# Mencetak kembali login_attempts untuk memastikan sudah direset ke 0
print(f"Jumlah percobaan login setelah direset: {user.login_attempts}")