# given some positive integer n, calculate the sum of the first n positive
# integer
def sum_of_n_positive_int(n):
    print("sum of first n positive integer:", "(", n, ")", sep="", end=", ")
    if n == 0:
        return 0
    else:
        return sum_of_n_positive_int(n - 1 ) + n


print(sum_of_n_positive_int(10))