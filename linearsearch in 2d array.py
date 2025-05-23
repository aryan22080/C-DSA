import numpy as np 
my_array2 = ([[1,2,3,],[4,5,6],[7,8,9]])
def linearsearch(array,target):
    for i in range(len(my_array2)):
        for j in range(len(my_array2)):
            if my_array2[i][j] == target:
                print("value found at position :"+ str(i) +" " + str(j))
    return -1
print(linearsearch(my_array2, 9))
    
