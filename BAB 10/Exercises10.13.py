import json

filename = 'user_profile.json'

def get_new_user_profile():
    """Meminta informasi pengguna baru dan menyimpannya dalam dictionary."""
    profile = {}
    profile['username'] = input("Masukkan nama pengguna: ")
    profile['age'] = input("Masukkan usia Anda: ")
    profile['hobby'] = input("Apa hobi utama Anda? ")
    
    with open(filename, 'w') as f:
        json.dump(profile, f)
    return profile

def greet_or_load_profile():
    """Membaca profil yang sudah tersimpan atau membuat yang baru."""
    try:
        with open(filename) as f:
            profile = json.load(f)
    except FileNotFoundError:
        profile = get_new_user_profile()
        print("\nProfil Anda berhasil dibuat dan disimpan!")
    else:
        print("\n--- Ringkasan Profil yang Diingat ---")
        print(f"Nama Pengguna : {profile['username']}")
        print(f"Usia          : {profile['age']}")
        print(f"Hobi          : {profile['hobby']}")

greet_or_load_profile()