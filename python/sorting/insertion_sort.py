def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]: # while we are at the 2nd element of the array and the 
# #             # element is  out of position or the element is greater than the previous element
            swap(j, j-1, arr)
            j -= 1
    return arr

# def swap(i, j, arr):
#     arr[i], arr[j] = arr[j], arr[i]

    

# if __name__ == '__main__':
#     print(insertion_sort([200, -234, 0, 2, 99, 1000, -18, 22, 1]))
