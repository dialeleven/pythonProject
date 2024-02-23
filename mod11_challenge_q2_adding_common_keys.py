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