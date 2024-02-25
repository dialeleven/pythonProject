def unique_count(tup):
    ''' input:tup-indicates the tuple
         output:Print the unique elements and their frequency'''
    
    # YOUR CODE GOES HERE

    # dictionary to track values in tup and frequency (key:index will be value:freq)
    freq_dict = {}

    #print(tup)

    for item in tup:
        # convert each item to a string for processing in case some db throws in something like a list (ok smart guy)
        item = str(item)
        
        # item (number) exists already in our dictionary, so check the counter (value) for the current key
        if item in freq_dict:
            #print('Processing:', item, ' in freq_dict')

            # get value for current key
            count = (freq_dict[item])
            
            # increment total count by 1
            count += 1

            # store new frequency counter for key
            freq_dict[item] = count
            #print('freq_dict[item]:', freq_dict[item])
        # current item (number) doesn't exist in our frequency dictionary, so frequency total is one
        else:
            #print('Processing: ', item, ' NOT IN freq_dict')
            freq_dict[item] = 1
            #print(f'item: {item}, freq_dict[{item}]: {freq_dict[item]}\n')

    # loop through our dictionary of numbers and frequencies (total count for each number) and ouput
    for dict_item in freq_dict:
        print(dict_item, ':', freq_dict[dict_item])

#unique_count( tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2) )
unique_count( tup = (1,2,3,2, "Hello", [4,8,16], "Hello") )
#unique_count( tup = (10, 8, 10, 15, 10, 2) ) 

'''
Frequency of unique elements
============================

Problem Description:
Write a function to print out the frequency of all the unique elements present in a given tuple.


Input Format:
The one input line consists of a tuple.


Output Format:

Unique elements and their frequencies are expected to be printed as follows:
unique_element1 : freq1
unique_element2 : freq2


Sample Input:

(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)


Sample Output:

10 : 3
8 : 4
5 : 2
2 : 2
15 : 1


CATCH THIS CASE!!
Your submission failed for the following input:
(1,2,3,2, "Hello", [4,8,16], "Hello")
'''
