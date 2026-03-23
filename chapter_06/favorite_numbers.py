f_numbers = {
    'max': [7, 14],
    'willow': [1,2],
    'miko': [2,3],
    'daria': [3,4],
    'marie': [4,5,6,7,8,9],
}

for name, numbers in f_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")
