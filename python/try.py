# def solve(A, result=0):
#     for i in range(len(A)):
#         for j in range(len(A)):
#             if A[i] == A[j]:
#                 result = max(result, abs(i - j))

#     return result


# print(solve([4, 6, 2, 2, 6, 6, 1]))


# def solving(a, result = 0):
#     hash = {}
#     for i, j in range(len(a)):
#         current = a[i]
#         next_item = a[j] + 1

#         hash[current] = True
#         if current == hash[current]:
#             result = max(result, abs(i - j))
#         print(hash)
#     return result
    

# print(solving([4, 6, 2, 2, 6, 6, 1]))




def plusMinus(arr, N ):
    # Write your code here
    positive_count = 0
    negetive_count = 0
    zero_count = 0
    N = len(arr)
    for i in range(N):
        if arr[i] < 0 and arr[i] > -101:
            negetive_count += 1
        if arr[i] == 0:
            zero_count += 1
        if arr[i] > 0 and arr[i] < 101:
            positive_count += 1 

    print(format(positive_count/ N, ".6f"))
    print(format(negetive_count / N,  ".6f"))
    print(format(zero_count / N,  ".6f"))

    print("..................................")
    print("positive count: ", positive_count)
    print("negetive count: ", negetive_count)
    print("zero count: ", zero_count)
    
    


plusMinus([-4, 3, -9, 0, 4, 1], 101)
arrays = [i for i in range(-100, 101)]
plusMinus(arrays, 100)

N = int(input())
listahan = input().split()
diks = {"pos": 0, "neg": 0, "zer": 0}
for i in listahan:
    if int(i) > 0:
        diks["pos"] += 1
    elif int(i) < 0:
        diks["neg"] += 1
    else:
        diks["zer"] += 1
print(format(diks["pos"]/N, '.3f'))
print(format(diks["neg"]/N, '.3f'))
print(format(diks["zer"]/N, '.3f'))
