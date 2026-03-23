print("Write two numbers to divide.")
print("Enter 'q' to quit.")

while True:
    first = input("First number: ")
    if first == 'q':
        break
    second = input("Second number: ")
    if second == 'q':
        break
    try:
        result = int(first)/int(second)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"{first}/{second}={result}")
