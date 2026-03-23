while True:
    age = input("What's your age? ")
    if age == 'quite':
        break
    age = int(age)
    if age < 3:
        print(f"Your ticket is free!")
    elif age < 12:
        print(f"Your ticket is $10!")
    else:
        print(f"Your ticket is 15!")
