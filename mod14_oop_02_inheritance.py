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
            Human.data.remove(self.name)
        else:
            print('This person has already passed')
    
    def child(self, number):
        Human.population += number


# Inheritance:
# Human is base (or parent) class
# Employee is derived (or child/extended) class
class Employee(Human):
    # re-initiate constructor (NOTE: This will NOT call the 'Human' constructor
    # which is why we have 'name' and 'age' as a parameter. Try it without
    # including 'name' and 'age' in the __init__ using the code:
    #    employee1 = Employee('Apple', 'CEO')
    # You will get "NameError: name 'name' is not defined."
    def __init__(self, name, age, company, position):
        # this will inherit the attributes 'name' and 'age' from 'Human' class
        super().__init__(name, age)

        # attribute for employee class
        self.company = company
        self.position = position
    
    # add some attributes
    def hire(self, person):
        print(f'{person} has been hired in our company')
        Human.data.append(person)
        Human.population += 1

    # another method to test out
    def leaveCompany(self):
        print(f'{self.name} has left the company')
        Human.population -= 1
        Human.data.remove(self.name)

# create instance of Human object
myhuman = Human('Sally', 35, 'Yoga')

# print attributes
print(myhuman.name)

# call greet() method of Human class
myhuman.greet()

# create another Human object instance
myhuman2 = Human('Bob', 40, 'Fitness')

print('population =', myhuman.population)
print('myhuman.data =', myhuman.data)

# hmm why use the 'Human' class name instead of the object 'myhuman'???
print('population =', Human.population)
myhuman.dead()
print('population =', Human.population)


# create object from child class "Employee" derived from parent "Human" class
employee1 = Employee('Steve Jobs', 50, 'Apple', 'CEO')

employee1.greet()
print('population =', Human.population)

# print list of humans
print('myhuman.data =', myhuman.data)

# call 'Employee' method 'hire'
employee1.hire('Joe Employee')


print('population =', Human.population)

# print list of humans
print('myhuman.data =', myhuman.data)

employee2 = Employee('Employee 2', 70, 'XYZ', 'Worker')
print('population =', Human.population)

# call dead() method from 'Human' class
employee2.dead()
print('population =', Human.population)

# employee has left the company
employee1.leaveCompany()
print('population =', myhuman.population)