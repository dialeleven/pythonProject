# Testing various OOP concepts
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


'''
Python super() Function
https://www.w3schools.com/python/ref_func_super.asp

Definition and Usage
The super() function is used to give access to methods and properties of a parent or sibling class.

The super() function returns an object that represents the parent class.
'''
class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)

class Child(Parent):
    #pass
    def __init__(self, txt):
      super().__init__(txt)


x = Child("Hello, and welcome!\n\n")

x.printmessage()



class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        # use super() function to access methods and properties on parent class. 
        # The super() function returns an object that represents the parent class. 
        super().method()  # Call the parent class's method
        print("Child method")
        pass

# Creating an instance of Child
child_obj = Child()

# Calling the method
child_obj.method()