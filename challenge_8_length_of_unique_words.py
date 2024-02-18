'''
https://www.scaler.com/topics/course/python-for-beginners/challenge/392636/challenge/?mode=read

Challenge 8 - Length of unique words

Problem Description:

Given two sentences, write a program to return the sum of the total number of unique words from each sentence.

Input Format:

The first line indicates the number of test cases.There will be two lines of inputs for each test cases as following:
The two lines consist of two sentences in string format.
Output Format:

The number of unique words from the sentences in integer format.
'''

def set_operation(sent1,sent2):
    ''' input:sent1,sent2-two sentences taken as inputs
         output:return the sum of length of unique words.'''
    
    # YOUR CODE GOES HERE
    unique_word_count = 0

    # split string based on space
    sent1_split = sent1.split()
    print(sent1_split)

    # loop through each word in the sentence
    for i in sent1_split:
        # unique word counter
        unique_word_count += 1

        # keep track of our unique words
        #unique_words
        print(i)


set_operation("hello world hello", "more and more data will be passively collected")
#set_operation("in data analysis we use data and process it further to create better interpreted data", "more and more data will be passively collected")

print('============')
mylist = ["apple", "banana", "cherry"]
print(mylist)
mylist += ["pear"]
print(mylist)