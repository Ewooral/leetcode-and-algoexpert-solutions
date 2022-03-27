myList = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# formula for finding the missing number of n series is n(n+1)/2 

def find_missing_n_series(array, n):
    sum1 = 30*31//2;
    # sum2 = sum(array);
    print(sum1 - sum2);

find_missing_n_series(myList, 31)