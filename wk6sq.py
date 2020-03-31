# James Hannon
# A function to get the square root of a number #non-Newton

def iamroot(x):
    ans = x ** .5
    return ans

x = float(input("Please enter an interger: "))


print ("The square root of ", x ,"is approx.", round(iamroot(x), 1))
