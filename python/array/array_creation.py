from array import *

arr1 = array('i', [1, 2, 3, 4, 5]);
arr2 = array('d', [4.2, 8.3, 0.2]);

# print(arr1);
# print(arr2);
# print(arr2[0]);



# INSERTION OPERATION

arr1.insert(0, 38);
print(arr1);

# Insertion doesn't delete a value but shifts the value to
# the right.

arr2.insert(3, 100.786);
print(arr2);

# Insertion at the end of an array is O(1) T and S complexity
# Insertion at the beginning or middle of an array is O(n)

# TRAVERSING AN ARRAY
def traverse_array(array):
    for element in array:
        print(element);

traverse_array(arr1);


# ACCESSING AN ELEMENT
def access_element(array, index):
    if index > len(array):
        print("The element doesn't exit")
    else:
        print(array[index])
