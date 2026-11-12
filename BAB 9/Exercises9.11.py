# File Utama: my_admin.py

from user_admin import Admin

# Membuat instance Admin
admin_baru = Admin("Budi", "Santoso", "budi_adm", "budi@example.com", "Surakarta")

# Menjalankan method untuk membuktikan semuanya berjalan dengan baik
admin_baru.describe_user()
admin_baru.privileges.show_privileges()