# NameError
#print(a)

# TypeError
#2 + '2'

# print list built-in functions, exceptions, and other objects of the Python interpreter
print(dir(__builtins__), '\n\n--------------\n')


a = 5
b = 0

try:
    res = a/b
    print(res)
except NameError:
  print("Variable is not defined")
# get type of exception using
except Exception as e:
    print(f'An error has occurred: {e}')
# else keyword - executed if nothing went wrong
else:
    print('Nothing went wrong')
finally:
    print('This is the "finally:" block which runs regardless if try is successful or except runs')


print('\n--------------\n')


#a = 5

try:
    print(x)
except NameError:
  print("Variable is not defined")
#except Exception as e:
#    print(f'An error has occurred: {e}')
except ZeroDivisionError:
    print("Division by zero error")
except:
    print('Something else went wrong')
# else keyword - executed if nothing went wrong
else:
    print('Nothing went wrong')