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
    # initialize some vars to avoid errors below
    unique_word_count = 0
    i = 0
    unique_words = []

    # store both sentences in list for iteration
    my_sentences = [sent1, sent2]
    
    # loop through both sentences
    for one_sentence in my_sentences:
        print(f"Sentence: {one_sentence}")
        
        # split sentence string based on space separator (default)
        sentence_split_words = one_sentence.split()
        print(sentence_split_words)




    # split sentence string based on space separator (default)
    sentence_split_words = sent1.split()
    print(sentence_split_words)


    # loop through each word in the sentence
    for current_word in sentence_split_words:
        #print(f"\n*** Current word being processed is '{current_word}' ***".upper())

        try:
            # check if current word in our unique_words list
            current_word_is_duplicate = current_word in unique_words
            
            # on first iteration, our first word will be considered unique
            if i == 0:
                unique_words = [current_word]
                unique_word_count += 1
                print(f"Current word '{current_word}' appears to be unique. i = {i}")
            # current word is not found (True/False for "in") in our list of unique words, so it's unique
            elif current_word_is_duplicate == False:
                print(f"Current word '{current_word}. current_word_is_duplicate = {current_word_is_duplicate}. ' .  i = {i}")
                
                # add it to our list of unique words
                unique_words += [current_word]

                # increment total unique word counter
                unique_word_count += 1

        # word was found in list already, so don't count it as a unique word
        except ValueError:
            print('***ValueError*** Hey {word} is unique, so let us keep track of it?')

        # keep track of our unique words
        #unique_words
        print(current_word)

        i += 1
    
    print('Unique word count for sentence 1 is:', unique_word_count)
    print(f'Sentence 1 is: {sent1}')
    print(f'Sentence 1 unique words are: {unique_words}')
    

sentence1 = "hello world hello how are you"
sentence2 = "more and more data will be passively collected"

#set_operation(sentence1, sentence2)
set_operation("in data analysis we use data and process it further to create better interpreted data", "more and more data will be passively collected")