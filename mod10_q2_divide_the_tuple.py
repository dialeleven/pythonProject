def odd_even_split_tuple(tup):
    ''' input:tup-indicates the tuple
         output:print two tuples one for even indexed and odd indexed in the given output format

         Sample Input:
            (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
         
         Sample Output:

         Odd: (10, 5, 10, 10, 5, 8)
         Even: (8, 2, 15, 8, 8, 2)
    '''
    
    # initialize vars
    counter = 0
    odd_elements, even_elements = [], []

    # YOUR CODE GOES HERE
    # loop through each tuple element
    for i in tup:
        # mod 2 with a zero remainder is an odd index
        if counter % 2 == 0:  
            odd_elements += [i]
        # even index
        else:
            even_elements += [i]
        
        # keep track of even vs. odd tuple index
        counter += 1
    
    # convert lists to tuple() now that we are done with the mutability of the list
    print('Odd:', tuple(odd_elements))
    print('Even:', tuple(even_elements))



# uncomment the line below to test it out
#odd_even_split_tuple( tup = tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)) )