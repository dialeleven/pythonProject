# print all vowels
text = "The quick brown fox jumped over the lazy dog"

for i in text:
   # check if letter is a vowel
   if "a" in i or "e" in i or "i" in i or "o" in i or "u" in i:
      print(i , end = '|')