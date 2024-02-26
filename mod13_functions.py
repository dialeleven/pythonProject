def greet(name):
    '''
    This function greets the user when called
    '''
    print(f'Hello {name}')
    '''
    This is a regular multi-line comment
    '''

greet('Sally')
print(greet.__doc__)


def intro(name, age, hobby):
    return name, age, hobby

# return multiple values as individual variables
a, b, c = intro('Sally', 30, 'Cycling')
print(a, b, c)

# return multiple values as a single return tuple "value"
d = intro('Sally', 30, 'Cycling')
print(d, '-', type(d))


a = 5

def func():
    global a
    a = 20
    print(a)

print(a) # a = 5 before func() call
func() # a = 20 within func()
print(a) # a= 20 outside func()


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


x = lambda a : a + 10
print(x(5))

y = lambda a, b : a + b
print(y(3, 4))


# function to return the larger of two numbers
def larger(a, b):
   if a > b:
        return a
   else:
      return b
   
print(larger(43, 5))


# lambda version to return the larger of two numbers
z = lambda x, y : x if x > y else y
print(z(50, 100))
print(z(25, 10))