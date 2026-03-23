from city_functions import city_country


def test_city_country():
    """Do names like 'Santiago, Chili' work?"""
    result = city_country('santiago', 'chili')
    assert result == 'Santiago, Chili'

def test_city_country_population():
    """Do names like 'Santiago, Chili - population 5000000' work?"""
    result = city_country('santiago', 'chili', 5_000_000)
    assert result == 'Santiago, Chili - population 5000000'
