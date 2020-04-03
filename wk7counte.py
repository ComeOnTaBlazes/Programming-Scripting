#James Hannon
#Input & Output

#with open ('e.txt', 'r') as f:
 #   data = f.read()

#below copied from: 
# https://www.computerhope.com/issues/ch001721.html

mylines = []

#count = 0

#letter = 0

with open ('Dogs.txt', 'r') as myfile:
    for line in myfile:
        x = line.count('e')
        mylines.append(x)

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
