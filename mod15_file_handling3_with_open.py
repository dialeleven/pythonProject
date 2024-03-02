with open('mod15_text.txt') as f:
    print(f.read())

print(f.closed)

with open('mod15_text.txt', 'w') as f:
    f.write('Writing to file again')


with open('mod15_text.txt') as f:
    print(f.read())