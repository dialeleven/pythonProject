'''
OOP - Inheritance
https://www.scaler.com/topics/course/python-for-beginners/video/656/

Working with a simplified Human class for polymorphism

Polymorphism in Python
- The word "polymorphism" means having many forms
- The same class method can work differently for different objects

- e.g. calling the makeSound() method can work differently for different objects
            - Cow object can call makeSound() to make a 'moo' sound
            - Cat object can call makeSound() to make a 'meow' sound

'''
class Human:
    # class variables
    population = 0
    data = []

    # constructor
    def __init__(self):
        # attributes of a human
        pass
    
    # methods
    def speak(self, language):
        print('I speak', language)

h1 = Human()
h2 = Human()

# the speak() method is working differently for different objects
h1.speak('English')
h2.speak('Korean')
