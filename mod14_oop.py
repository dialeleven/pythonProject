class Car:
    pass

honda = Car()
print(type(honda))


class Human:
    # constructor
    def __init__(self, name, age, hobby):
        # attributes of a human
        self.name = name
        self.age = age
        self.hobby = hobby
    
    # methods
    def greet(self):
        print(f'Hey my name is {self.name}')

myhuman = Human('Sally', 35, 'Yoga')

print(myhuman.name)
print(myhuman.age)
print(myhuman.hobby)

myhuman.greet()
