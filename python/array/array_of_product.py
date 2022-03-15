# T = O(n^2), S = O(n)
def array_of_product(array):
    # products = [1 for _ in range(len(array))];
    final_products = [None] * len(array);

    for i in range(len(array)):
        currentProduct = 1;
        for j in range(len(array)):
            if i != j :
                currentProduct *= array[j]
        final_products[i] = currentProduct
    return final_products

print(array_of_product([5, 1, 4, 2]))  # [8, 40, 10, 20] 

# T = O(n), S = O(n)
def array_of_product2(arr):
    leftProduct, rightProduct, product = [1] * len(arr), [1] * len(arr), [1] * len(arr)
    # print(left, right, product)
    left_product = 1   
    for i in range(len(arr)):
        leftProduct[i] = left_product
        left_product *= arr[i]
    right_product = 1
    for i in range(len(arr)-1, -1, -1):
        rightProduct[i] = right_product
        right_product *= arr[i]

    for i in range(len(arr)):
        product[i] = leftProduct[i] * rightProduct[i]
    return product


print(array_of_product2([5, 1, 4, 2]))  # [8, 40, 10, 20]
