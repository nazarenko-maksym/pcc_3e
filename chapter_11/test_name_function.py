from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Tom Cruise' work?"""
    formatted_name = get_formatted_name('tom', 'cruise')
    assert formatted_name == 'Tom Cruise'

def test_first_last_middle_name():
    """Do names likes 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
