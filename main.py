a = int(input('Write the 1st side of triangle = '))
b = int(input('Write the 2nd side of triangle = '))
c = int(input('Write the 3rd side of triangle = '))
if a + b < c and  b + c < a and a + c < b:
    print('Triangle exist')
else: print('Triangle doesn\'t exist')