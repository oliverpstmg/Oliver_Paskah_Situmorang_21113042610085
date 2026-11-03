def make_sandwich(*items):
    """Mencetak ringkasan bahan-bahan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(profil := f"- {item}")

# Memanggil fungsi dengan jumlah argumen yang berbeda-beda
make_sandwich('keju', 'tomat', 'selada')
make_sandwich('daging sapi', 'keju')
make_sandwich('telur', 'mayones', 'mentimun', 'saus BBQ')