from name_function import get_formatted_name

print("Enter 'q' any time to quit.")
while True:
    first = input("Write first name: ")
    if first == 'q':
        break
    last = input("Write last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tFormatted name: {formatted_name}.")
