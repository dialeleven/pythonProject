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


# sorting a list with tuples
lst = [(12, 56), (2, 4), (5,3)]

# sorts based on the first index of each tuple (e.g. 2, 5, 12)
lst.sort() 
print(lst)
#>>> [(2, 4), (5, 3), (12, 56)]

# function to return index 1 of the passed value
def getkey(x):
   return x[1]

# sort our list above [(12, 56), (2, 4), (5,3)] using the 2nd index (1)
lst.sort(key = getkey)
print(lst)
#>>> [(5, 3), (2, 4), (12, 56)]


# lambda version of above
lst.sort(key = lambda x : x[1])
print(lst)
# >>> [(5, 3), (2, 4), (12, 56)]


def mix(a, b, c, age = 25, *arg, **kwargs):
    print(a, b, c)
    print(age)
    print(arg)
    print(kwargs)

mix(2, 4, 6, 45, 10, 12, 14, name='Sally', hobby = 'Swimming')


def convert(t):
    return t*9/5 + 32

print(convert(20))

def fun1(name, age):
   print(name, age)

fun1("Mohit", age=23)
fun1(age = 23, name="Mohit")
#fun1(name="Mohit", 23)
fun1(23, "Mohit")

def Interest(p,c,t=2,r=0.09):
  return p*t*r

print(Interest(c=4,r=0.12,p=5000))