from pathlib import Path

path = Path('learning_python.txt')

content = path.read_text()
print(content)

content_c = content.replace('Python', 'C')
print(content_c)
