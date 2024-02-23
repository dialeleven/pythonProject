thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

for item in thisset:
    print(item, end=' ')
print()

thisset.add('mango')

for item in thisset:
    print(item, end=' ')
print()


thisset = {"apple", "banana", "cherry"}
thisset.remove('banana')
print(thisset, end=' ')