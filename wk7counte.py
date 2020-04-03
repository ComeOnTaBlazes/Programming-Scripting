#James Hannon
#Input & Output
#I have not had the time to ge this code working as I would like

#create a list
mylines = []

#ask user for filename to be sacnned
userinput = input("Please enter a file you want to analyze:")
#run a error test on what the user has input, return text if error
#and re-direct to userinput request

#ask user for what they want to scan the file for
#countstr = input("Please enter what you would like to count: ")


#open file from userinput as read
with open (userinput, 'r') as myfile:
    #for individual line in the file
    for line in myfile:
        #make all characters lowercase and create lines
        lines = line.lower()
        #count all occurances of e in lines
        x = lines.count('e')
        #append number to list
        mylines.append(x)
        
        
#sum each value in list together
print(sum(mylines))
   
   