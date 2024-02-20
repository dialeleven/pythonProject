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