# main.py

from utilsPackage.utils import *

if __name__ == "__main__":
    # Call the function and store what it returns 
    #  in a variable called data
    data = read_CSV_file()
    print("# of rows in data set", len(data))
    #Print the first and last row
    print("First Row: ", data[0])
    print("Last Row: ", data[-1])
    
    #Write a list comprehension expression 
    #To pull out all the collision types into a set
    
    collisionTypes = {myData[6] for myData in data}
    print("# of collision types: ", len(collisionTypes))
    print(collisionTypes)
    
    #For Thursday, Modify ^ expression to prevent the blank type of collision

