sentence = 'Hello World'
excited = True

def volume_sphere(r):
    '''input: r = Input in integer format
       output:return Vol of sphere upto two decimals'''
    # YOUR CODE GOES HERE
    r = float(r)
    Vol=(4 * (22/7) * r ** 3) / 3

    return Vol

radius = input('Enter radius: ')
volume = volume_sphere(radius)

print('Volume is', volume)