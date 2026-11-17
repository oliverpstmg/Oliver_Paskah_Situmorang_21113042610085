
def city_country(city, country, population=None):
    """Mengembalikan string dengan format 'Kota, Negara – population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"