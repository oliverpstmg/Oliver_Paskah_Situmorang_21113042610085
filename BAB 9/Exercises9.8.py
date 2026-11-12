
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "dapat menambah postingan", 
                "dapat menghapus postingan", 
                "dapat memblokir pengguna"
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("Daftar Hak Istimewa (Privileges):")
        for privilege in self.privileges:
            print(f"- {privilege}")

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nProfil: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Halo, {self.first_name}!")

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        # Menjadikan class Privileges sebagai atribut di dalam Admin
        self.privileges = Privileges()

# Membuat instance Admin baru dan mengakses method show_privileges melalui atribut privileges
admin_baru = Admin("Andi", "Pratama", "andi_adm", "andi@example.com", "Surabaya")
admin_baru.describe_user()
admin_baru.privileges.show_privileges()