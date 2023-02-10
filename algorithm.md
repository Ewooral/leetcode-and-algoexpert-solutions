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
    1 for j D 2 to A:length
    2 key D AŒj 
    3 // Insert AŒj  into the sorted sequence AŒ1 : : j  1.
    4 i D j  1
    5 while i>0 and AŒi > key
    6 AŒi C 1 D AŒi
    7 i D i  1
    8 AŒi C 1 D key
    ```
