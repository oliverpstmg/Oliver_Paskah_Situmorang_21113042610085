import json

def get_stored_username(filename):
    """Mengambil nama pengguna yang tersimpan jika ada."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    """Meminta nama pengguna baru dan menyimpannya."""
    username = input("Masukkan nama pengguna baru: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Menyapa pengguna dengan verifikasi identitas."""
    filename = 'username.json'
    username = get_stored_username(filename)
    
    if username:
        # Menanyakan konfirmasi kepada pengguna
        correct = input(f"Apakah Anda {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(filename)
            print(f"Kami akan mengingat Anda saat kembali, {username}!")
    else:
        username = get_new_username(filename)
        print(f"Kami akan mengingat Anda saat kembali, {username}!")

greet_user()