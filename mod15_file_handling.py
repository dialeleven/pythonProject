f = open('mod15_text.txt')
#print(f.closed)
contents = f.read()
print(contents)
f.close()
print(f.closed)

# file opening modes
#f.write('hello') # this will fail without the 'w' mode parameter


f = open('mod15_text.txt', 'w')

# this will return a number indiciating the length of the string written to the file
f.write('Writing to file again')