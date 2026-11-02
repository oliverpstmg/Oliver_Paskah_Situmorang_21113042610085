"""Contoh program yang mematuhi standar PEP 8."""

def calculate_rectangle_area(length, width):
    """Menghitung luas persegi panjang berdasarkan panjang dan lebar."""
    area = length * width
    return area


def print_welcome_message(name):
    """Mencetak pesan sambutan personal untuk pengguna."""
    print(f"Selamat datang di modul pemrograman, {name}!")


# Blok utama program
if __name__ == '__main__':
    print_welcome_message("Mahasiswa Teknik Industri")
    result = calculate_rectangle_area(10, 5)
    print(f"Luas area: {result}")