'''
Function to calculate the volume of a sphere given a radius 'r'
The volume of a sphere having radius R is given by (4 * π * R3) / 3.

NOTE: Return the volume of the sphere up to two decimal places. You can use round().
NOTE2: Use pi as 22/7 (not math.pi).
'''
def volume_sphere(r):
    '''input: r = Input in integer format
       output:return Vol of sphere upto two decimals'''
    # YOUR CODE GOES HERE
    r = float(r)
    Vol = (4 * (22/7) * r ** 3) / 3
    Vol = round(Vol, 2)1.5

    return Vol

radius = input('Enter radius of sphere (whole number or float only please): ')
volume = volume_sphere(radius)

print('The volume of the sphere with a radius of', radius, 'is', volume)
