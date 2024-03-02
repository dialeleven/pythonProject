with open('mod15_text.txt') as f:
    data = f.read()
    print(data)

with open('mod15_text.txt') as f:
    # read first N characters
    data = f.read(5)
    print(data)

    # read next N characters
    data = f.read(5)
    print(data)

    # tell - tell you the position of your file handle
    pos = f.tell()
    print('file position is:', pos)
    
    # read rest of characters
    data = f.read()
    print(data)

    # using seek() method you can reset your file handler
    f.seek(0)
    f.seek(3)
    data = f.read()
    print(f.tell())
    print(data)

# using readlines() method
with open('mod15_textnew.txt', 'r') as f:
    f.seek(0)
    data = f.readlines()
    print(data)

    # loop through list and output
    for line in data:
        print(line)