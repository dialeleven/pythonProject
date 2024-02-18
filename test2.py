name = 'Jimmuy'
print('J' in name)

if (True):
   print('this is true')
else:
   print('this is false')


n = int(input('Enter an integer'))

mod2_result = n % 2

# n / 2 does not give a remainder of zero, so it's not an even number
if mod2_result != 0:
    print(f'Weird {mod2_result}')
# n is even and in the inclusive range of 2 to 5, print Not Weird
elif mod2_result == 0 and (n >= 2 and n <= 5):
    print('Not Weird')
# If n is even and in the inclusive range of 6 to 20, print Weird
elif mod2_result == 0 and (n >= 6 and n <= 20):
    print('Weird')
    #print('Weird - stmt 3')
# n is even and greater than 20
elif mod2_result == 0 and n > 20:
    print('Not Weird')
    #print('Not Weird - stmt 4')
else:
    print(f'Nothing to see. n = {n}.')