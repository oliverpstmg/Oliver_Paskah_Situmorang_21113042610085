# test_cities.py

from city import city_country


def test_city_country():
  """Does a city like 'santiago, chile' work correctly?"""
  santiago_chile = city_country('santiago', 'chile')
  assert santiago_chile == 'Santiago, Chile'


def test_city_country_population():
  """Can we include a population argument?"""
  santiago_chile = city_country('santiago', 'chile', population=5000000)
  assert santiago_chile == 'Santiago, Chile – population 5000000'