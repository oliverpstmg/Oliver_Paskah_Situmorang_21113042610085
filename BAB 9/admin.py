# Modul: admin.py

from user import User

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

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()