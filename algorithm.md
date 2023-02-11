# Insertion sort
    Our first algorithm, insertion sort, solves the sorting problem introduced in Chapter 1:
    Input: A sequence of n numbers (a1; a2;:::;an).
    Output: A permutation (reordering) has
    1; a0
    2;:::;a0
    ni of the input sequence such
    that a0
    1 a0
    2 a0
    n.
    The numbers that we wish to sort are also known as the keys. Although conceptually we are sorting a sequence, the input comes to us in the form of an array with n
    elements.
    In this book, we shall typically describe algorithms as programs written in a
    pseudocode that is similar in many respects to C, C++, Java, Python, or Pascal. If
    you have been introduced to any of these languages, you should have little trouble
## What separates pseudocode from “real” code is that in
    pseudocode, we employ whatever expressive method is most clear and concise to
    specify a given algorithm
## pseudocode is not typically concerned with issues of software engineering.
    Issues of data abstraction, modularity, and error handling are often ignored in order
    to convey the essence of the algorithm more concisely.
# insertion sort
    is an efficient algorithm for sorting a small number of elements. 
    This sorting algorithm works the way people sort a hand of playing cards
### INSERTION-SORT.A/
    ```python
        def insertion_sort(arr):
            for i in range(1, len(arr)):
                j = i
                while j > 0 and arr[j] < arr[j-1]:
                    swap(j, j-1, arr)
                    j -= 1
            return arr


       def swap(i, j, arr):
            arr[i], arr[j] = arr[j], arr[i]

    ```
