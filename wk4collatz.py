# User to input any positive integer and outputs
# The successive values of the following calculation
# input/result even /2, if odd *3 and add 1

# Create a list
L = []

x = float(input("Please enter an interger (Hint: it's 10): "))
#m = 2

L.append(x)

while x != 1:
    if x % 2 == 0:
        x /= 2
        L.append (x)
    else:
        x = (3 * x) + 1
        L.append (x)

print (L)

#if x % 2 == 0:
   # print (x / 2)
#else:
 #   print ((x * 3) +1)
