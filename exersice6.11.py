cities = {
    'surakarta': {
        'country': 'indonesia',
        'population': '522.000 jiwa',
        'fact': 'Dikenal sebagai Kota Batik dan Kota Budaya.'
    },
    'yogyakarta': {
        'country': 'indonesia',
        'population': '415.000 jiwa',
        'fact': 'Terkenal sebagai kota pelajar dan pusat budaya Jawa.'
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta jiwa',
        'fact': 'Merupakan salah satu wilayah metropolitan terpadat di dunia.'
    }
}

for city, info in cities.items():
    print(f"Kota: {city.title()}")
    print(f"\tNegara   : {info['country'].title()}")
    print(f"\tPopulasi : {info['population']}")
    print(f"\tFakta    : {info['fact']}\n")