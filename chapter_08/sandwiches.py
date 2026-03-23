def make_sandwich(*ingredients):
    print('Making sandwich with:')
    for ingredient in ingredients:
        print('-', ingredient)

make_sandwich('bread')
make_sandwich('bread', 'lettuce')
make_sandwich('bread', 'lettuce', 'tomato', 'pepperoni')
