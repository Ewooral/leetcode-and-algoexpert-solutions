def binarySearch(array, item):
    # In binary search the array must always be sorted!
    array.sort();
    low = 0;
    high = len(array) - 1;
    while low <= high:

        mid = (low + high) // 2;  # index of the mid item
        guess = array[mid];  # middle item

        if guess == item:
            print( f"item { item } found at index: { mid }");
            return item;

        elif guess > item:
            high = mid - 1;

        else:
            low = mid + 1;
    return None;


def isEven():
    number = binarySearch(array, item);
    if number is None: return "isEven: ", -1;

    if number % 2 == 0:
        return "isEven: ", True; 
    return "isEven: ",  False;


if __name__ == '__main__':
    array = [8, 2, 0, 1, 4, -2, 9, 7, 12];
    item = 8;
    # array.sort();
    # print("Sorted array: ", array);
    print(binarySearch(array, item));
    # print(array.index(8));
    print(isEven());


def recursiveBinarySearch(low, high, array, item):
    array.sort();
    if low <= high:

        mid = (low + high) // 2;  # index of the mid item
        guess = array[mid]; # middle item

        if guess == item:
            return f"item { item } found at index: { mid }"
        elif guess > item:
            return recursiveBinarySearch(low,  mid - 1, array,  item)

        else:
            return recursiveBinarySearch(mid + 1, high, array, item);


    return -1;


if __name__ == '__main__':
    array = [8, 2, 0, 1, 4, -2, 9, 7, 12];
    item = 8;
    low = 0;
    high = len(array) - 1;
    print(recursiveBinarySearch(low, high, array, item));
    
   
