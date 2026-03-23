active = 0

while True:
    age = input("What's your age? ")
    if age == 'quite':
        break
    age = int(age)
    if age <= 0 or age >= 100:
        break
    active += 1
    if active > 10:
        break
    if age < 3:
        print(f"Your ticket is free!")
    elif age < 12:
        print(f"Your ticket is $10!")
    else:
        print(f"Your ticket is 15!")
