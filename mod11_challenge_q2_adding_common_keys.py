def commonKey(dict1, dict2):
    '''dict1, dict2 are the two dictionaries
       print the required dictionary'''
    
    # dictionary for common keys
    dict3 = {}

    #YOUR CODE GOES HERE
    # loop through dict1
    for key in dict1:
        # key in dict1 exists in dict2
        if key in dict2:
            #print(key, ':', dict1[key], ' - ', key, ':', dict2[key])

            # sum the values of d1+d2
            sum = dict1[key] + dict2[key]

            # update dict3
            dict3.update( {key: sum} )
    
    print(dict3)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

#dict1 = {'my': 100654121, 'name': 21314351, 'is': 5484542, 'nisarg': 21351}
#dict2 = {'nisarg': 1021516516, 'who': 4151651846} # expected return value ==> {'nisarg': 1021537867}

commonKey(dict1, dict2)


'''
Adding Common Keys (https://www.scaler.com/topics/course/python-for-beginners/challenge/377544/challenge/?mode=read)

Problem Description:

Given two dictionaries, write a program for creating a dictionary in such a way that it consists of all the keys that are common in both dictionaries. The values corresponding to the keys in this new dictionary are the sum of the values of those keys in the two dictionaries.


Input Format:

The input contains four lines.
The first line is space-separated string values which are the keys of the first dictionary.
The second line is space-separated integer numbers which are values of the first dictionary.
The third line is space-separated string values which are the keys of the second dictionary.
The second line is space-separated integer numbers which are values of the second dictionary.


Output Format:

Print the resultant dictionary containing added values for common keys.


Sample Input:

a b c
1 2 3

c d e
4 5 6


Sample Output:

{'c': 7}


Output Explanation:

Given the two dictionaries, {'a': 1, 'b': 2, 'c': 3} and {'c': 4, 'd':5. 'e', 6}, key 'c' is common having values 3 and 4. 
Therefore, their sum 7 with the key 'c' should be added in to the resultant dictionary.
'''