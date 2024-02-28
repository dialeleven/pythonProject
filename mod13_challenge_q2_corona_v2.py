'''
https://www.scaler.com/topics/course/python-for-beginners/challenge/377714/challenge/

Time to end Corona

Problem Description
Given three integers, A, B and C. You have to find the number of days it will take to reach zero cases of Corona in a city.

A - Average cases recovered in a day of the corona.
B - Number of new cases of corona daily.
C - Current active cases of the corona.

Return the minimum number of days it will take to reach 0 active cases of Covid.

Problem Constraints

1 <= B < A <= 5000
1 <= C <= 1000


Input Format

The first argument will be integer A, which denotes the recovered cases in a day.
The second argument will be integer B, which denotes the new cases in a day.
The third argument will be integer C, which denotes the currently active cases.


Output Format

Return an integer which denotes the minimum days to reach 0 cases.


Example Input

Input 1:
A = 5
B = 3
C = 1

Input 2:
A = 4
B = 3
C = 2


Example Output

Output 1:
1

Output 2:
2


Example Explanation

Explanation 1:
At the end of Day 1, 3 new cases of Covid will arise. 
So, total cases at the end of Day-1 before recovery will be 1 + 3 = 4.
And after recovery there will be (4 - 5) = -1 cases, since there cannot be negative number of cases
the cases would be 0 at the end of Day 1

Explanation 2:
At the end of Day 1, before recovery, cases will be 2 + 3 = 5.
After recovery 5 - 4 = 1 case
At the end of Day 2 before recovery,cases will be 1 + 3 = 4.
After recovery 4 - 4 = 0 case


The first argument will be integer A, which denotes the recovered cases in a day.
The second argument will be integer B, which denotes the new cases in a day.
The third argument will be integer C, which denotes the currently active cases.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        recovered_cases = A
        new_cases = B
        active_cases = C
        days = 1

        # total cases before recovery
        total_cases = new_cases + active_cases

        # total cases after recovery
        cases_after_recovery = total_cases - recovered_cases

        # if we have zero cases or a negative number of cases (e.g. # of recoveries > total_cases - recovered_cases)
        if cases_after_recovery <= 0:
            return 1
        
        # calculate days to recover
        while active_cases > 0:
            # total cases before recovery
            total_cases = new_cases + active_cases

            # total cases after recovery
            active_cases = total_cases - recovered_cases

            # increment the total number of days
            days += 1

        # exclude final counter increment at 0 or less cases otherwise days count is off by +1
        days -= 1
        

        #print(f'A/B/C: {A}/{B}/{C}, total_cases:', total_cases, ', cases_after_recovery: ', cases_after_recovery)
        return days


'''
The first argument will be integer A, which denotes the recovered cases in a day.
The second argument will be integer B, which denotes the new cases in a day.
The third argument will be integer C, which denotes the currently active cases.
'''
#print ( Solution.solve(None, A = 5, B = 3, C = 1) ) # output = 1
#print ( Solution.solve(None, A = 4, B = 3, C = 2) ) # output = 2
print ( Solution.solve(None, A = 50, B = 49, C = 8) ) # output = 8