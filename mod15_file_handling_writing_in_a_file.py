# create new (or overwrite existing file)
with open('mod15_textnew.txt', 'w') as f:
    f.write('Hey new file')

# create new (or overwrite existing file) - notice the above file is overwritten
with open('mod15_textnew.txt', 'w') as f:
    f.write('This is updated content now.\n')
    f.write('More strings on another line.\n')


with open('mod15_textnew.txt', 'a') as f:
    f.write('Appending a line to an existing file.')