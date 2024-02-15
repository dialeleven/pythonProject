'''
Find maximum in a list
https://www.scaler.com/topics/course/python-for-beginners/video/622/
'''
marks = [90, 30, 100, 50, 80, 95]

# iterate through list
highest = marks[0] # index 0 will be = 90 from the list above

#highest will be 90
#print(highest)

for i in marks:
   # check the condition
   if i > highest:
      highest = i

print('The highest mark is', highest, 'from the list of', marks)