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


Sample Input:

1
in data analysis we use data and process it further to create better interpreted data
more and more data will be passively collected

Sample Output:
20

Sample explanation:
{'use', 'process', 'create', 'better', 'analysis', 'in', 'it', 'further', 'and', 'we', 'data', 'interpreted', 'to'} 
represent the 13 unique words from sentence1 and {'collected', 'more', 'be', 'and', 'data', 'passively', 'will'} 
represent the 7 unique words from sentence2. Therefore 13 + 7 = 20 is returned.

Note:
If a word is present in both sentences it should be counted separately for both sentences.
'''

def set_operation(sent1, sent2):
    ''' input:sent1,sent2-two sentences taken as inputs
         output:return the sum of length of unique words.'''
    
    # YOUR CODE GOES HERE
    # initialize some vars to avoid errors below
    unique_word_count = 0 # counter for total number of unique words in a sentence; reset after each sentence
    unique_words = [] # Track the unique words in a sentence. Make sure to reset after each sentence!

    # store both sentences in list for iteration in for loop
    my_sentences = [sent1, sent2]
    
    # loop through both sentences
    for single_sentence in my_sentences:
        print(f"Sentence: {single_sentence}")
        
        # split sentence string based on space separator (default)
        sentence_split_words = single_sentence.split()
        #print('Sentence.split() = ', end = '')
        #print(sentence_split_words)

        # loop through each word in the sentence
        for current_word in sentence_split_words:
            #print(f"\n*** Current word being processed is '{current_word}' ***".upper())

            try:
                # check if current word in our unique_words list
                current_word_is_duplicate = current_word in unique_words
                
                # Current word is not found (True/False for "in") in our list of unique words, so it's unique.
                # Store the current word in a list, total number of unique words
                if current_word_is_duplicate == False:
                    # add it to our list of unique words
                    unique_words += [current_word]

                    # increment total unique word counter
                    unique_word_count += 1

                    # debug output
                    #print(f"Current word '{current_word}.' current_word_is_duplicate = {current_word_is_duplicate}. unique_word_count = {unique_word_count}")
                # current word is a duplicate, so nothing to do (other than debugging output)
                else:
                    None
                    #print(f"Current word '{current_word}.' current_word_is_duplicate = {current_word_is_duplicate}. unique_word_count = {unique_word_count}")
            #/end try
                    
            # word was found in list already, so don't count it as a unique word
            except ValueError:
                print('***ValueError*** Hey {current_word} is unique, so let us keep track of it?!?')
        # /end for
        
        # OUTPUT OUR UNIQUE WORDS FOR DEBUGGING
        print(f'total_unique_word_count = {unique_word_count}')
        print('Unique words: ', end='')
        print(unique_words, end = '\n\n')
        
    
        unique_words = [] # Track the unique words in a sentence. Make sure to reset after each sentence!
    
    #print(f'Grand total unique_word_count is {unique_word_count}')

    return unique_word_count
###### end def #####


sentence1 = 'in data analysis we use data and process it further to create better interpreted data'
#sentence1 = "hello world hello how are you"
sentence2 = 'more and more data will be passively collected'


# call function to process both sentences and return the total number of unique words in EACH sentence
total_unique_words = set_operation(sentence1, sentence2)

print(total_unique_words)