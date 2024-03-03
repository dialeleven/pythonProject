filename = 'mod15_textnew.txt'

with open(filename, 'w') as f:
    f.write('Let us try another file now\n')

with open(filename, 'r') as f:
    data = f.read()
    print(data)


with open('mod15_textnew.txt', 'a') as f:
    f.write('Appending a line to an existing file.')

with open(filename, 'r') as f:
    data = f.read()
    print(data)