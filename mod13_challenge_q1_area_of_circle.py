'''
https://www.scaler.com/topics/course/python-for-beginners/challenge/377714/challenge/

Find the Area of Circle
Problem Description:

Write a function to calculate and return the area of a circle by using the radius of the circle given as a parameter.

Notes:

 Round up the area to 2 decimal places. You can use the round() function.
 Use pi as 3.14159.
 You need not take input in this problem, you need to only implement the function provided.
Input Format:

The first line indicates the number of the test cases. 
For each test case there will be one line of input in integer format representing radius.
Output Format:

Area in float format rounded upto 2 decimal places for each testcase.
Sample Input:

1  
5
Sample Output:

78.54
 

Sample explanation:

The area for circle with radius 5cm is 3.14159 x (5 x 5) = 78.53975 cm2

After rounding by 2 digits, it becomes 78.54 cm2
'''
def circle_area(r):
    ans=None
    '''input: r = A numerical value as radius
       output: Return the area of circle as ans upto 2 decimal places'''
    # YOUR CODE GOES HERE

    ans = 3.14159 * (r * r)
    ans = round(ans, ndigits=2)

    return ans

print(circle_area(5))