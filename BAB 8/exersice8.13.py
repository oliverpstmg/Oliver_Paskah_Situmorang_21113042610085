def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Membuat profil diri sendiri
my_profile = build_profile(
    'budi', 'santoso',
    major='Teknik Industri',
    university='Universitas Sebelas Maret',
    hobby='Pemrograman'
)

print(my_profile)