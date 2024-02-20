mylist = [2, 4, 6, 8, 10]

for i in mylist:
    print(i)

print(mylist[::])
print(mylist[0:3:])
print(mylist[2::])
print(mylist[::-1])
print(mylist[::-2])

fruits = ['apple', 'cherry', 'banana', 'cherry']
print ( fruits.count("cherry") )

try:
    print (fruits.index('appleZZZ'))
except ValueError:
    pass
    #print('not in the list!')