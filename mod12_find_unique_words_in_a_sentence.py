# find unique words in a sentence
sentence = 'Be the change you wish to see in the world'

mylist = sentence.split()
print(len(mylist), mylist)

# set() function creates a set object.
myset = set(mylist)
print(len(myset), myset)