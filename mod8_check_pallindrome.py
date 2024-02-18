print("This program will check if a string is a pallindrome (same word spelled backwards - e.g. radar, mom, noon).\n\n")
text = input("Try typing in a word to test it out: ")

'''
# loop through each letter
for i in text:
    print (i, end = '')
'''

j = 1
reversed_string = ''

# loop through each letter
for i in text:
    reversed_string += text[-j]
    #print(text[-j])
    j += 1

if (text == reversed_string):
    print(f"Your word \"{text}\" spelled backwards is \"{reversed_string}\" which is a PALLINDROME!")
else:
    print(f"Sorry, your word \"{text}\" spelled backwards is \"{reversed_string}\" which is NOT a pallindrome.")













'''
for i in text:
   # check if letter is a vowel
   if "a" in i or "e" in i or "i" in i or "o" in i or "u" in i:
      print(i , end = '|')
'''