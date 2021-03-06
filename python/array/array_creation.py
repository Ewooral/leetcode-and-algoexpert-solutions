from array import array


arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('d', [4.2, 8.3, 0.2])

print(arr1);
print(arr2);
print(arr2[0]);


# INSERTION OPERATION

arr1.insert(0, 38)
print("Inserting at the beginning of the array: ", arr1)

# Insertion doesn't delete a value but shifts the value to
# the right .

arr2.insert(3, 100.786)
print(arr2)

# Insertion at the end of an array is O(1) T and S complexity
# Insertion at the beginning or middle of an array is O(n)

# TRAVERSING AN ARRAY


def traverse_array(array):
    for element in array:
        print(element)


# # O(n) T complexity | O(1) S complexity
traverse_array(arr1);


# ACCESSING AN ELEMENT
def access_element(array, index):
    if index >= len(array):
        print("The element doesn't exit")
    else:
        print(array[index])


access_element(arr2, 2)
# Time and Space Complexity: O(1)


# SEARCHING FOR EXISTING ELEMENT IN AN ARRAY
def search(array, item):
    for element in array:
        if element == item:
            return True, array.index(item);
    return False

# O(n) T complexity | O(1) S complexity

print(search(arr1, 2))


# SEARCH A VALUE BY IT'S INDEX
def search_by_index(array, index):
    for i in range(0, len(array)):
        # print(i)
        if i == index:
            return True, array[index]
    return "Index doesn't exist'"


print(search_by_index(arr1, 3)) 


# # DELETE AN ELEMENT FROM THE ARRAY
def delete_element(array, index):
    del array[index]
#     # or array.remove(element)
    return array

# # O(n) T complexity | O(1) S complexity


print(delete_element(arr1, 3))
print(search_by_index(arr1, 3))

# using the count() method to remove duplicates
newArray = array('i', [1,4,3,6,2,7, 2, 3,2,1,0,4,4,6])
newArray1 = array('i', [1, 3, 6, 3, 2, 6, 1, 2, 3, 1, 4, 5,  6, 2, 0])
def removeDuplicates(arr):
    hashset = set();
    for i in arr:
        hashset.add(i);
        newlist=list(hashset);
    print(newlist);
        



removeDuplicates(newArray);
removeDuplicates(newArray1);

def DupRemove(array):
    temp = [];
    for i in array:
        if i not in temp:
            temp.append(i);
    return temp;


print(DupRemove(newArray1));

