from pathlib import Path


filenames = ['cats.txt', 'no_file.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text().strip()
        words = contents.split()
    except FileNotFoundError:
        print(f"File \"{filename}\" does not exist.")
        # pass
    else:
        print(contents)
        print(f"File \"{filename}\" has {len(words)} words.")
