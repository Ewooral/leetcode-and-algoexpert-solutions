def linear_search(arr, item):
    for element in arr:
        if element == item:
            return element
    return None


print(linear_search([1, 3, 6, 8, 2], 0))
