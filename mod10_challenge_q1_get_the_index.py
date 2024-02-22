def get_index(tup, elem):
    ''' input:elem-indicates the element in the tuple,tup-indicates the tuple
         output:Return the index of the element.'''
    
    # YOUR CODE GOES HERE
    # element value exists in tuple; check needed to avoid "ValueError: tuple.index(x): x not in tuple"
    if elem in tup:
        theindex = tup.index(elem)
        return theindex
    else:
        return -1

# two sample function calls below
theindex = get_index((10, 20, 30, 40, 50), 50) # index exists (4)
theindex = get_index((10, 20, 30, 40, 50), 100000) # index doesn't exist (-1)
print(theindex)