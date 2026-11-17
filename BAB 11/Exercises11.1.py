# File: test_cities.py

from city_functions import city_country

def test_city_country():
    """Apakah kota seperti 'santiago, chile' dapat diformat dengan benar?"""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'