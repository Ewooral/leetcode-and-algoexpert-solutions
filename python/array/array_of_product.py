def array_of_product(array):
    # products = [1 for _ in range(len(array))];
    products = [1] * len(array);

    for i in range(len(array)):
        runningProduct = 1;
        for j in range(len(array)):
            if i != j :
                runningProduct *= array[j];
        print(runningProduct)
        products[i] = runningProduct;


    return products
 

print(array_of_product([5, 1, 4, 2]))



