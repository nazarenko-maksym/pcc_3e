from pathlib import Path

path = Path('pi_digits.txt')
content = path.read_text()

for line in content.splitlines():
    print(line.strip())
