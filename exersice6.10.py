favorite_numbers = {
    'ani': [7, 11],
    'budi': [14, 5, 8],
    'citra': [3],
    'dodi': [9, 21],
    'eka': [21, 4, 12]
}

for name, numbers in favorite_numbers.items():
    print(f"Angka favorit {name.title()} adalah:")
    for number in numbers:
        print(f"\t{number}")
    print()