cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for number in cubes:
    print(number)


cubes = [number ** 3 for number in range(1, 11)]

for number in cubes:
    print(number)
