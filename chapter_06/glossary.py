glossary = {
    'variable': 'named storage location in a computer memory',
    'function': 'named block with input, task and output',
    'if': 'conditional statement',
    'for': 'a loop cycle for iteration on data',
    'list': 'an array of data stored in computer memory as continious block',
    'dict': 'data structure (dictionary) that stores key:value pairs',
    'set': 'data structure that stores unique values in no particular order',
    'string': 'data structure that stores sequence of characters',
}

for key, value in glossary.items():
    print(f"{key.title()}:\n\t{value.capitalize()}.")
