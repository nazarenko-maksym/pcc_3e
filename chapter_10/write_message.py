from pathlib import Path

content = 'hello world!\n'
content += 'I love creating new games.\n'
content += 'I also love working with data.\n'

path = Path('programming.txt')
path.write_text(content)
