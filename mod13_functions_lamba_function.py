# lambda version to return the larger of two numbers
z = lambda x, y : x if x > y else y
print(z(50, 100))
print(z(25, 10))

'''
Syntax
    lambda arguments : expression

The expression is executed and the result is returned:
'''