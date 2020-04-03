# James Hannon
# Create program to confirm if today is a weekday

# Import datetime
import datetime

x= datetime.datetime.now().weekday()

#test of if formula
#x = 5


#print (x)

# Weekday values in tuple list
Wkday = range (0, 5)

#x = datetime.datetime.now().weekday()

if x in Wkday:
    print ("Today is a weekday")
else:
    print ("Today is a weekend")