import numpy as np 
my_array2 = ([[1,2,3,],[4,5,6],[7,8,9]])
print(my_array2)
new_array = np.delete(my_array2,0,axis=0)
print(new_array)
