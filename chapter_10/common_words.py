from pathlib import Path


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
word_to_count = input("Write the word you want count in files: ").lower()

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text().strip()
        words = contents.split()
    except FileNotFoundError:
        print(f"File \"{filename}\" does not exist.")
        # pass
    else:
        print(f"The \"{filename}\" has:")
        print(f" - {len(words)} words")
        print(f" - \"{word_to_count}\" appears {contents.lower().count(word_to_count)} times")
