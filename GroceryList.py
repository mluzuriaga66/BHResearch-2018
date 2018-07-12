import numpy as np
import pandas as pd
#declaring the variable to open the file
#f = open("grocerylist.txt", "w")
#writing the file
#f.write("strawberry, blueberry, greek yogurt")

#reading the grocery list file
#f = open("grocerylist.txt", "r")
#printing the grocery list file
#print f.write()
#f.close()

#declaring the varaible "f" to open the file, and W is to wite in the file
f = open("grocerylist.txt","w")
#creating multiple linesat once, these are the what are in a yogurt parfait
lines_of_text=["strawberry ","blueberry ","granola ","greek yogurt "]
f.writelines(lines_of_text)
#closing the file
#f.close()


#opening the txt file and reading it
f = open("grocerylist.txt","r")
#printing the list
print f.readlines()

#appending the file
#f = open("grocerylist.txt","a")
#f.write("i still don't get this")
#f.close()

#have the grocery list aka the WRITE in print out in a column
f = open("grocerylist.txt","w")
for i in lines_of_text:
    f.write(str(i)+'\n')
    print i

f.close()
