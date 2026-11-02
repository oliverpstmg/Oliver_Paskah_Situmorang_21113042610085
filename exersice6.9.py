favorite_places = {
    'budi': ['pantai', 'gunung', 'kafe'],
    'siti': ['perpustakaan', 'taman kota'],
    'joko': ['stadion']
}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name.title()} adalah:")
    for place in places:
        print(f"\t- {place.title()}")
    print()