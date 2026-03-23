languages = ['ukrainian', 'english', 'mandarin', 'hindi', 'spanish', 'french', 'arabic', 'begali', 'portuguese']

print(len(languages))
print(f"The languages.pop() return \"{languages.pop()}\" language")
languages.insert(0, 'polish')
print(f"To insert another language to the beginning of the list, we use languages.insert(0, 'polish') and the list now is {languages}")
print(f"sorted() can be used to keep the original order of list, but get the sorted version: {sorted(languages)}")
print(f"sorted(reverse=True) can be used to keep the original order of list, but get the sorted version in reverse order: {sorted(languages, reverse=True)}")
languages.sort()
print(f".sort() mutates the list permanently: {languages}")
languages.sort(reverse=True)
print(f".sort(reverse=True) mutates the list permanently in reverse order: {languages}")
