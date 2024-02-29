'''
OOP - Inheritance
https://www.scaler.com/topics/course/python-for-beginners/video/656/

General info
- When a class derives all attributes and methods from another class
    -It gets access to all its methods and attributes
    - This helps in reusability of code
    - e.g. a "Human" class can derive a class such as "Employee" that inherits all attributes and methods from the "Human" class
        - Human class (base or parent class)
            - Employee class (derived class)
            - Boss class


Working with the Human class for inheritance
'''
class Human:
    # class variables
    population = 0
    data = []

    # constructor
    def __init__(self, name, age, alive = True):
        # attributes of a human
        self.name = name
        self.age = age
        self.alive = alive

        # increment population for EVERY new Human object
        Human.population += 1

        # add each name of Human object to a list
        Human.data.append(self.name)
    
    # methods
    def greet(self):
        print(f'Greetings, {self.name}!')
    
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

# call greet() method of Human class
myhuman.greet()


# print value of class variable
print('myhuman.population =', myhuman.population)


# create another Human object instance
myhuman2 = Human('Bob', 40, 'Fitness')
print('myhuman.population =', myhuman.population)

# print list of humans
print('myhuman.data =', myhuman.data)


print('Human.population =', Human.population)
myhuman.dead()
print('Human.population =', Human.population)

myhuman3 = Human('Adam', 25)
print('Human.population =', Human.population)

myhuman.child(2)
print('Human.population =', Human.population)


# Inheritance
class Employee(Human):
    pass

# create object from child class "Employee" derived from parent "Human" class
employee1 = Employee('Steve Jobs', 50)
print('Human.population =', Human.population)

employee1.greet()

# print list of humans
print('myhuman.data =', myhuman.data)
