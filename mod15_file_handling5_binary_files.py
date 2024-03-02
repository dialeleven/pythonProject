# open image (binary file) in read and binary mode
with open('mod15_test.png', 'rb') as f:
    data = f.read()
    print(data)

    with open('mod15_testnew.png', 'wb') as d:
        d.write(data)