from pathlib import Path


name = input("Write your name: ")

path = Path('guest.txt')
path.write_text(name)
