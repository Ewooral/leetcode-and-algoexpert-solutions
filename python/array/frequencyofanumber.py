arr = [1, 2, 8, 2, 2, 2, 5, 1]
fr = [None] * len(arr)
print(fr)
visited = -1
for i in range(0, len(arr)):
    # print(i)
    count = 1
    for j in range(i + 1, len(arr)):
        # print(j)
        if arr[i] == arr[j]:
            count += 1
            # to avoid counting the same element again,
            fr[j] = visited
        if fr[i] != visited:
            fr[i] = count

#Displays the frequency of each element present in array  
print("---------------------");  
print(" Element | Frequency");  
print("---------------------");  
for i in range(0, len(arr)):
    if fr[i] != visited:
        print(arr[i], " | ", fr[i]);

print("---------------------");
    


# The frequency of an element can be counted using two loops.
#One loop will be used to select an element from an array,
#  and another loop will be used to compare the selected element with the rest of the array.