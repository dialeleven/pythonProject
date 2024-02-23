def returnSum(dict):
    sum = 0
    
    # PRINT THE SUM OF VALUES
    # YOUR CODE GOES HERE
    for key in dict:
        sum += dict[key]
    
    print(sum)

returnSum({ 'x': 25, 'y': 25, 'z': 50})


'''
Sum of Values (https://www.scaler.com/topics/course/python-for-beginners/challenge/377544/challenge/?mode=read)

Problem Description:

Given a dictionary, find the sum of values of every key in the dictionary.


Input Format:

The input contains two lines.
The first line has space-separated string values which are the keys of the dictionary.
The second line has space-separated integer numbers which are the values of the dictionary.


Output Format:

Print the sum of the values of the items as an integer.


Sample Input:

x y z
25 25 50


Sample Output:

100


Output Explanation:

The dictionary has three key-value pairs having values 25, 25, and 50. Hence their sum, 25+25+50 = 100 should be printed.
'''