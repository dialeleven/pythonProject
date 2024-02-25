x = {"apple", "banana", "cherry"}
y = {"banana", "microsoft", "apple"}
z = x.intersection(y) 

print(z, end='\n')

# union example (this only inserts UNIQUE items)
group1 = {'Thor', 'Hulk', 'Cap'}
group2 = {'Falcon', 'Cap', 'Iron Man' }

group3 = group1.union(group2)
print(group3)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Python Set difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)



x = set(("apple", "banana", "cherry"))

print(x)

# Note: the set list is unordered, so the result will display the items in a random order.


fruits = { 'apple' : 120, 'mango' : 100, 'banana' : 90 }
new_fruits = { 'peach' : 130, 'kiwi' : 80 }
fruits.update(new_fruits)
print(fruits)

sets = {3, 4, 5} 
sets = sets.union({1, 2, 3})
print(sets)



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple\n")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict["color"] = "blue"
print(thisdict)

sets = {3, 4, 5} 
sets.update([1, 2, 3])
print(sets)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}


thisset.update(tropical)


print(thisset)


group1 = {'1', '2', '3'}
group2 = {'4', '5', '6' }


group3 = group1.union(group2)
print(group3)
