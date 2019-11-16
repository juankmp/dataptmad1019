


import sys

#print ('1')

#a = sys.argv[0]
#print(a)

#b = float(sys.argv[1])
#c = float(sys.argv[2])

#d = b + c
#print(d)

square = lambda x: x*x

def squarer_f(x):
    return x**2

square_1 = [square(x) for x in range(1,10)]
square_2 = [squarer_f(x) for x in range(1,10)]

print(square_1)
print(square_2)


