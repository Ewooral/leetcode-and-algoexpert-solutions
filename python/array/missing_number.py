myList = [1, 2, 3, 6, 7, 8, 9, 10, 11, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# formula for finding the missing number of n-series = n(n+1)/2
# find the sum() of the array => sum(array)
# subtract sum of array from n-series and you have your answer

def find_missing_n_series(array, n):
    sum1 = 30*31//2;
    sum2 = sum(array);
    print(sum1 - sum2);

find_missing_n_series(myList, 31);

def missingNumber(array):
    for index, value in enumerate(array): # n, n+ 1
        print(index, value)
        if value - index > 1:
            newValue = value - 1
            return newValue
    return []


print(missingNumber(myList));




