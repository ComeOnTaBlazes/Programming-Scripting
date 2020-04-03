#James Hannon
#square using Newton's method
#f(x) = x**2 - a with derivative of f(x) = 2x
#


def f(x):
    return x**2 - a

def df(x):
    return 2 * x

#l = []

a = float(input("Enter an integer: "))

#start with an approximation/guess
x = 5

#iterate through cycles to get better approximation
for val in range(6):
    x1 = x - (f(x)/df(x))
    #l.append(x)
    x = x1

#print(l)
print("The square root of ", a, "is approx. ", round(x,1))

