'''
Second Largest

Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.


Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 109

Input Format
The first argument is an integer array A.

Output Format
Return the second largest element. If no such element exist then return -1.

Example Input
Input 1:
A = [2, 1, 2] 

Input 2:
A = [2]


Example Output
Output 1:
1 

Output 2:
-1 


Example Explanation
Explanation 1:

    First largest element = 2
    Second largest element = 1

Explanation 2:

    There is no second largest element in the array.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # reverse sort list (largest to smallest)
        A.sort(reverse=True)

        # total number of elements in list
        total_elements = len(A)
        
        # get largest number in list
        largest_num = A[0]

        # total number of largest number in list
        largest_num_count = A.count(largest_num)

        # only one element, so there's no 2nd largest element/number
        if total_elements == 1:
            return -1
        # Handle cases where A is like [2, 2] or [2, 2, 2] where it's the same number multiple times; naughty naughty.
        elif largest_num_count == total_elements:
            return -1
        else:
            #print(A)
            #print(f'largest_num = {largest_num} and occurs {largest_num_count} time(s)')

            # Loop through N times the number of occurrences of the largest number (e.g. [2, 1, 2, 2] we have 3 occurrences of "2").
            # Pop off the first element until the largest number is gone
            for i in range(largest_num_count):
                #print(f'hello i = {i}')
                A.pop(0)
            
            _2nd_largest_num = A[0]

            return _2nd_largest_num


integer_array = [2, 1, 2]
integer_array = [2, 1, 99, 3, 7, 100]
#integer_array = [2, 2, 2]
#integer_array = [2]

# get the 2nd largest number in the list
return_val = Solution.solve(None, integer_array)

print(return_val)