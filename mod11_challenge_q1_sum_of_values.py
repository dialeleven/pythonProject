def returnSum(dict):
    sum = 0
    
    # PRINT THE SUM OF VALUES
    # YOUR CODE GOES HERE
    for key in dict:
        sum += dict[key]
    
    print(sum)

returnSum({ 'x': 25, 'y': 25, 'z': 50})