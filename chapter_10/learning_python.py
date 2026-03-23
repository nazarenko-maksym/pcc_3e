from pathlib import Path

path = Path('learning_python.txt')

content = path.read_text()
print(content)

content_lines = path.read_text().splitlines()
for line in content_lines:
    print(line)
