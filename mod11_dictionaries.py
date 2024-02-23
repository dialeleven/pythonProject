mydict = {}
print(type(mydict))
print(mydict)

mydict = dict()
print(type(mydict))
print(mydict)

# create a dictionary using {}
fruits = {
    'apple' : 120,
    'mango' : 100,
    'banana' : 90
}

for key in fruits:
    print(key, ':', fruits[key])
print(fruits , end = '\n===========\n\n')


# dictionary using dict() constructor
mydict = dict(name = 'Jim', age = 50, country = 'USA')
print(type(mydict))
print(mydict , end = '\n===========\n\n')


# creating dictionary using zip() function
name = ['apple', 'mango', 'banana']
prices = [120, 100, 90]

fruits = dict(zip(name, prices))
print(fruits)


# updating dictionary with update()
fruits = { 'apple' : 120, 'mango' : 100, 'banana' : 90 }
new_fruits = { 'peach' : 130, 'kiwi' : 80 }
fruits.update(new_fruits)
print(fruits)
print(fruits.popitem())
print(fruits)

print(len(fruits))

# remove last key-value pair added
fruits = { 'apple' : 120, 'mango' : 100, 'banana' : 90 }
print(fruits)
print(fruits.popitem())
print(fruits)

# check if key is in dictionary
print('apple' in fruits)
print('pineapple' in fruits)

fruits = { 'apple' : 120, 'mango' : 100, 'banana' : 90 }

# remove an object in python (dictionary, object, etc)
#del(fruits)
#print(fruits)

# iterate through dictionary using key and dictionary 
for key in fruits:
    print(key, fruits[key])

# make a "shallow copy" of the dictionary
'''
You cannot copy a dictionary simply by typing dict2 = dict1, 
because dict2 will only be a reference to dict1, and 
changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy:
- one way is to use the built-in Dictionary method copy()
- another way to make a copy is to use the built-in function dict()
'''
fruits_copy = fruits.copy()
print(fruits_copy)

fruits['apple'] = 1000
print('fruits:', fruits)
print('fruits_copy:', fruits_copy)



# shallow copy example (https://realpython.com/copying-python-objects/)
print('-----\nshallow copy example')
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy
print('xs:', xs)
print('ys:', ys)

xs.append(['new sublist'])
print('xs:', xs)
print('ys:', ys)
print("After xs[1][0] = 'XYZ'")
xs[1][0] = 'XYZ'
print('xs:', xs)
print('ys:', ys)


# deepcopy example (https://realpython.com/copying-python-objects/)
print('-----\ncopy.deepcopy(obj) example')
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

print('xs:', xs)
print('zs:', zs)
print("After xs[1][0] = 'X'")
xs[1][0] = 'X'
print('xs:', xs)
print('zs:', zs, end = '\n\n\n')


# using the .copy() method to create a shallow copy
print("Using the .copy() method to create a shallow copy")
fruits = { 'apple' : 1, 'mango' : 2, 'banana' : 3 }
fruits_copy = fruits.copy()
#fruits_copy = fruits

print('fruits:', fruits)

fruits['apple'] = 1000
print("After fruits['apple'] = 1000")
print('fruits:', fruits)
print('fruits_copy:', fruits_copy, end = '\n\n\n')


# using = to create a 'reference' copy
print("Using the = to create a 'reference' copy")
fruits = { 'apple' : 1, 'mango' : 2, 'banana' : 3 }
fruits_copy = fruits
#fruits_copy = fruits

print('fruits:', fruits)

fruits['apple'] = 1000
print("After fruits['apple'] = 1000")
print('fruits:', fruits)
print('fruits_copy:', fruits_copy, end = '\n\n\n')


d = {'r' : 1, 'r' : 3, 'r' : 10}
print(d['r'])


dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}

val = dict1['age']

#print(val)

if 'age' in dict1:
    print('This is a member of the dictionary')
else:
    print('This is not a member of the dictionary')

# Changing Attributes
# Which of the following is the correct way of changing the ‘salary’ of ‘smit’ to 8500?
freshers = {
    'student1': {'name': 'yash', 'salary': 7500},
    'student2': {'name': 'heet', 'salary': 8000},
    'student3': {'name':'smit', 'salary': 6500}
}

print(freshers)
freshers['student3']['salary'] = 8500
print(freshers)

bbt = {'Sheldon': 1, 'Leonard': 2}
bbt.update({'Penny': 2})
print(bbt)