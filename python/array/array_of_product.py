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


def array_of_product2(arr):
    left, right, product = [1] * len(arr), [1] * len(arr), [1] * len(arr)
    print(left, right, product)

array_of_product2([1,5,3,4,2])
