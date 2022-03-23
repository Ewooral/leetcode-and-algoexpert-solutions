import numpy as np; # install numpy and import it

# Creating a 2d array
twoDarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

# O(1) and O(m*n) T and S complexity respectively
print(twoDarray);  


print("...............................................");

# INSERT A COLUMN/ROW IN A 2D ARRAY
newtwoDarray = np.insert(twoDarray, 1, [[10, 11, 12]], axis=0);
print(newtwoDarray);

# O(m*n) or O(1) and O(1) T and S complexity respectively

print("...............................................");

# APPEND
# Append a row or a column at the end of the array using the append method
# if axis = 0, append will happen at the row, and axis = 1 at the column
newtwoDarray = np.append(twoDarray, [[13, 14, 15]], axis=0);
print(newtwoDarray);



print("...............................................");

# Accessing an element or a given cell in a 2d array 

def access_element(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array):
        print("Index out of range");
    else:
        return array[rowIndex, columnIndex];
    
# O(1) T and S complexity
print("The accessed element is: ", access_element(newtwoDarray,  1, 2));


print("...............................................");

# Traversing a 2d array

def printElement(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i, j]);
    return;

# O(m*n) and O(1) T and S complexity respectively
printElement(newtwoDarray); # this prints all items in the array


print("...............................................");

# Searching an element 
def printElement(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return value;
#     return None;

# # O(m*n) and O(1) T and S complexity respectively
# print(printElement(newtwoDarray, 9))


# print("...............................................");

# Deleting an item in a 2d array
newtwoDarray = np.delete(twoDarray, 1, axis=0);

# O(1) or O(m*n) and O(1) T and S complexity respectively
print("row or column deleted!\n", newtwoDarray);
