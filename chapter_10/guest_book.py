from pathlib import Path

names = []
while True:
    name = input("Write your name: ")
    if name == 'q':
        break
    names.append(name)

names_str = ""
for name in names:
    names_str += f"{name}\n"

path = Path('guest_book.txt')
path.write_text(names_str)
