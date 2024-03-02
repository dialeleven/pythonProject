# open image (binary file) in read and binary mode
with open('mod15_test.png', 'rb') as f:
    data = f.read()
    print(data)

    # take our existing binary data and write to a new copy of the file!
    with open('mod15_testnew.png', 'wb') as d:
        d.write(data)