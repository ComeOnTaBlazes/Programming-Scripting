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



with open (userinput, 'r') as myfile:
    for line in myfile:
        line.lower()
        x = line.count('e')
        mylines.append(x)
        y = line.count('E')
        mylines.append(y)
        

print(sum(mylines))
   
   # x = myfile.read(letter)
    #if x = 'e'
     #       counter += 1
    #elif x = 'E'
     #       counter += 1
    #else letter += 1
    #end =""
    
    
    #list = [line.strip() for line in myfile]
    #print(list)
