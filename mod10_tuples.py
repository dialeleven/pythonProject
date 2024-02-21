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


# list to tuple and tuple to list
print(t)
print(type(t))
mylist = list(t)
print(type(mylist))

t = tuple(mylist)
print(t)
print(type(t))