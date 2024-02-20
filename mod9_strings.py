mylist = [2, 4, 6, 8, 10]

for i in mylist:
    print(i)

print(mylist[::])
print(mylist[0:3:])
print(mylist[2::])
print(mylist[::-1])
print(mylist[::-2])

fruits = ['apple', 'cherry', 'banana', 'cherry']
print ( fruits.count("cherry") )

fruits = ['apple', 'orange', 'banana']
fruits.insert(0, 'watermelon')
print(fruits)

fruits = ["apple", "banana", "cherry"]
new_list = [1, 2, 3]
fruits.append(new_list)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

mylist = ['apple', 12345, True, 3.14]
print(type(mylist[1]))
print(type(mylist[3]))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined_lists = [list1, list2, list3]

for i in combined_lists:
    for j in i:
        print (j, end = ' ')
    print()

print(combined_lists[0][1])
    #print(i)

print(fruits)
print(len(fruits))

mylist = ["a", "b", "a", "c", "c"]
print(mylist)
mylist = list(dict.fromkeys(mylist))
print(mylist)
print()
print()


fruits = ['apple', 'cherry', 'banana', 'cherry']
print(fruits)
print ( fruits.count("cherry") )
fruits.remove('cherry')
fruits.remove('cherry')
print(fruits)
fruits.sort(reverse=True)

players = ['Jadeja','Rahul','Rohit']
#players[len(players):] = ['Dhoni', 'Virat']
players+=['Dhoni', 'Virat']
print(players)

players = ['Jadeja','Rahul','Rohit']
players[len(players):] = ['Dhoni', 'Virat']
print(players)