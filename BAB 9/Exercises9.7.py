class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nProfil: {self.first_name} {self.last_name} (@{self.username})")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = [
            "dapat menambah postingan", 
            "dapat menghapus postingan", 
            "dapat memblokir pengguna"
        ]

    def show_privileges(self):
        print(f"\nHak Istimewa (Privileges) untuk Admin {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Membuat instance Admin dan memanggil method show_privileges()
admin_user = Admin("Siti", "Rahma", "siti_admin", "siti@example.com", "Bandung")
admin_user.describe_user()
admin_user.show_privileges()