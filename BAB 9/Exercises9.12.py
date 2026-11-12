

from admin import Admin

# Membuat instance Admin
admin_utama = Admin("Siti", "Rahma", "siti_admin", "siti@example.com", "Yogyakarta")

# Memanggil method untuk memastikan semua modul saling terhubung dan bekerja dengan benar
admin_utama.describe_user()
admin_utama.greet_user()
admin_utama.privileges.show_privileges()