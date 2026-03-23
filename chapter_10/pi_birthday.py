from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text().splitlines()
pi_string = ''
for line in contents:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

path_mln = Path('pi_million_digits.txt')
contents_mln = path_mln.read_text().splitlines()
pi_string_mln = ''
for line in contents_mln:
    pi_string_mln += line.lstrip()

print(f"{pi_string_mln[:52]}...")
print(len(pi_string_mln))

birthday = input("Write your birthday in yymmdd: ")
if birthday in pi_string_mln:
    print("Your birthday appears in first million digits of pi!")
else:
    print("Your birthday does not appears in first million digits of pi!")
