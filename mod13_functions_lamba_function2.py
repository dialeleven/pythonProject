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

'''
The sort() method sorts the list ascending by default.

You can also make a function to decide the sorting criteria(s).

Syntax
list.sort(reverse=True|False, key=myFunc)

================
Parameter Values
================

Parameter	    Description
---------------------------
reverse	        Optional. reverse=True will sort the list descending. Default is reverse=False
key	            Optional. A function to specify the sorting criteria(s)
'''