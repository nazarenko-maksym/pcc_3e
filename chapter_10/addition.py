print("Write two numbers to add.")
try:
    first = int(input("Write first number: "))
    second = int(input("Write second number: "))
    result = first + second
except ValueError:
    print("Write only digits! Letters doesn't work.")
else:
    print(f"{first}+{second}={result}")
