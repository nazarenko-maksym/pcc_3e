print("Write two numbers to add.")

while True:
    try:
        first = input("Write first number: ")
        if first == 'q':
            break
        first = int(first)
        second = input("Write second number: ")
        if second == 'q':
            break
        second = int(second)
        result = first + second
    except ValueError:
        print("Write only digits! Letters doesn't work.")
    else:
        print(f"{first}+{second}={result}")
