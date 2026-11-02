def city_country(city, country):
    """Mengembalikan string berformat 'Kota, Negara'."""
    return f"{city}, {country}"

# Memanggil fungsi dan mencetak nilai yang dikembalikan
city1 = city_country('Santiago', 'Chili')
city2 = city_country('Paris', 'Prancis')
city3 = city_country('Kyoto', 'Jepang')

print(city1)
print(city2)
print(city3)