'''
OOP basics.

Creating the following:
- classes: e.g. Car, Human
- objects: e.g. myhuman = Human('Sally', 35, 'Yoga')
- constructor: __init__
- attributes: e.g. self.name
- methods: e.g. greet()
- class variables: e.g. population
- instance variables: e.g. myhuman.name
- calling class methods - e.g. myhuman.greet()
'''
class Car:
    pass

honda = Car()
print(type(honda))


class Human:
    # class variables
    population = 0
    data = []

    # constructor
    def __init__(self, name, age, hobby, alive = True):
        # attributes of a human
        self.name = name
        self.age = age
        self.hobby = hobby
        self.alive = alive

        # increment population for EVERY new Human object
        Human.population += 1

        # add each name of Human object to a list
        Human.data.append(self.name)
    
    # methods
    def greet(self):
        print(f'Hey my name is {self.name}')
    
    def dead(self):
        if self.alive:
            print(self.name, 'is now more now.')
            Human.population -= 1
            self.alive = False
        else:
            print('This person has already passed')
    
    def child(self, number):
        Human.population += number

# create instance of Human object
myhuman = Human('Sally', 35, 'Yoga')

# print attributes
print(myhuman.name)
print(myhuman.age)
print(myhuman.hobby)

# call greet() method of Human class
myhuman.greet()

# you can even add an attribute outside of the class (interesting)
myhuman.nationality = 'Canadian'
print(myhuman.nationality)

# print value of class variable
print('myhuman.population =', myhuman.population)


# create another Human object instance
myhuman2 = Human('Bob', 40, 'Fitness')
print('myhuman.population =', myhuman.population)

# print list of humans
print('myhuman.data =', myhuman.data)


print(Human.population)
myhuman.dead()
print(Human.population)

myhuman3 = Human('Adam', 25, 'Sports')
print(Human.population)

myhuman.child(2)
print(Human.population)
