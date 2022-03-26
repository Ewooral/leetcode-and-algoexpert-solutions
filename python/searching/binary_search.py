def binarySearch(array, item):
    # In binary search the array must always be sorted!
    array.sort();
    low = 0;
    high = len(array) - 1;
    while low <= high:

        mid = (low + high) // 2;
        guess = array[mid];

        if guess == item:
            # return f"item { item } found at index: { mid }";
            return item;

        elif guess > item:
            high = mid - 1;

        else:
            low = mid + 1;
    return None;

def isEven():
    number = binarySearch(array, item);
    if number is None: return -1;

    # if number % 2 == 0:
        return True; 
    return False;

if __name__ == '__main__':
    array = [8, 2, 0, 1, 4, -2, 9, 7, 12];
    item = 71;
    array.sort();
    print("Sorted array: ", array);
    print(binarySearch(array, item));
    print(array.index(8));
    print(isEven());


