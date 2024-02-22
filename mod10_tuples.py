planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet, end=' ')
print('\n')

planets[0] = 'Merrrrcury'
for planet in planets:
    print(planet, end=' ')
print('\n')

# tuples use parentheses instead of square brackets like with lists (e.g. fruits = ['apple', 'pear', 'mango'])
planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
#planets[0] = 'Merrrrcury'
for planet in planets:
    print(planet, end=' ')
print('\n')

print(type(planets))

t = ([1, 3, 5 ,7], 'Jimbo')
print(t)
print(type(t))

t[0][0] = 100
print(t)

#t[0] = 'abc' # not allowed - "TypeError: 'tuple' object does not support item assignment"


a = 2
b = 4
c = 8

# different way to create variables
a, b, c = 2, 4, 8
print(a)
print(b)


# unpacking tuple exampe
t = (1, 2, 3, 4)
a, b, c, d = t
print(a, b, c, d, end='\n\n')

print( len(t), end='\n\n' )
print( t.index(1), end='\n\n')

for i in t:
    print(i * 2)

print( t * 2, end='\n\n')


# create a list using list() constructor
mylist = list(('a', 'b', 'c', 'd'))  # note the double round-brackets
print(mylist)
print(type(mylist), end = '\n\n')


# convert tuple to list
t = (1, 2, 3, 4)
print('t =', t)
print(type(t), '\n')
t = list(t)
print('t =', t)
print(type(t), '\n\n')


t = list((1, 2, 3, 4))
print('t =', t)
print(type(t), '\n\n')


# convert list to tuple
t = tuple(mylist)
print(t)
print(type(t))

# tuple concatenation
t = (1, 2, 3, 4)
t1 = (5, 6)
t2 = t + t1
print(t2)

t2 = t2 + t1
print(t2)

print(t2 * 2)

name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")
print(tup)

elements = (10, 20, 30, 40, 50, 60, 70, 80)
print(elements[2:5], elements[:4], elements[3:100])