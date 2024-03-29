## REVERSE WORDS IN STRINGS .....................................

1. inputs: 
        
            words = "good god is alive"
            startOfword = 0
            reverse_word = []
        
    - loop through the input string and keep track of the start of the each character. Assume the start of word = 0.

            for index in range(len(words)):
                ......

2. Convert the string to a list

    - When looping, if you encounter a whitespace " ", append from the start of the string to the current 
      string (words[startOfword:index])
    - update **startOfword** from 0 to where our index currently points

            if words[index] == " ":
                reverse_word.append(words[startOfword:index])
                startOfword = index

    - When the current index points to a whitespace in the string, append the whitespace or empty string into the reversed_word array

            if words[startOfword] == " ":
                reverse_word.append(" ")
                startOfword = index
                
3. Write a reverse function to swap both **start** word and **end** word in the list and convert the list back to a string using the **join** string method

            start, end = 0, len(list) - 1;
            while start < end:
                list[start], list[end] = list[end], list[start];
                start += 1;
                end -= 1;

4. Output:
        
        reverse_word = "alive is god good"





## GENERATE A DOCUMENT FROM A STRING..............................

1. input

        characters = "lolodgoai anwoidsdppdiieafidow soieh"

        document = "goal of the day"

2. Loop thru the document and save every character in a *char* variable 

3. At each character in the document, find the frequency of the character
in both the document and characters variables/identifiers
        
        already_counted = set()
        for c in document:
            if c in already_counted:
                    continue
            frequency_char_Doc = FC(char, document)
            frequency_char_Chars = FC(char, characters)


4. if document Frequency > characters frequency, return False,

        if frequency_char_Doc > frequency_char_Chars:
            return False
        already_counted.add(c)

5. Frequency of character

        def FC(char, target):
        frequency = 0
        for c in target:
            if c == char:
                frequency += 1
        return frequency


6. return True if everything pans out successfully

        OPTMISE THE CODE
    - use a **set()**

    - use a hash table **{}**

        * loop thru characters string
         - if a char in the **characters** string is not in the hash table, set the value of the character to 0
         - continue to increment value by 1

        * loop thru document string.
         - if a char in the document string is not in the hash table, or if a character value in the hash table is 0, return false
         - reduce character value in the hash table by 1
            characters[char] -= 1

                characters = {  
                    "char 1": 0 + 1,
                    "char 2": 0 - 1
                 }
        * return True




## BALANCE BRACKET..........................................

1. input

        stack = []

        string = "(abc)"
        openingBracket = "{(["
        closingBracket = "])}"
        matchingBracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
2. loop thru string
    * if a character in the string is in the opening bracket, append it in the stack
    * if a character in the string is in the closing bracket,
        - check if the stack is empty, return False 
        - if the last element in the stack is equal to character value in the matching Bracket dictionary, pop it off the stack
        - else, return False

                if stack[-1] == matchingBrackets[char]:
                   stack.pop()
                else:
                    return False

3. return True if stack is empty and False if not empty
        
        return len(stack) == 0. or True if len(stack) < 1 else False


# Create a Graph Class
1. Check if the graph is None. If yes, create it else, initialize it

         from collections import defaultdict
         from dataclasses import dataclass
         
         @dataclass
         class Graph:
            graph: dict = None
            if graph is None: 
               graph = defaultdict
            else:
               graph = None

            def addVertex(self, vertex, edge):
                  self.graph[vertex].append(edge)

# Breadth First Search Algorithm.........................

1. Initialize an empty **queue** and enqueue the starting **vertex** in it
   and mark the vertex as **visited**
        
            def Search(vertex):
               queue = [vertex]
               visited = [vertex]

2. while the queue is not empty, dequeue the first vertex from the queue

            dequeue = queue.pop(0)
            print(dequeue)

4. For each neighbor of the dequeued item, if the neighbor is unvisited
             
            for neighbor in graph[dequeue]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor) 



# Depth First Search Algorithm.............................

1. Initialize an empty **stack** and enqueue the starting **vertex** in it
   and mark the vertex as **visited**
        
            def Search(vertex):
               stack = [vertex]
               visited = [vertex]

2. while the stack is not empty, pop the first vertex from the stack

            popStack = stack.pop()
            print(dequeue)

4. For each neighbor of the dequeued item, if the neighbor is unvisited
             
            for neighbor in graph[dequeue]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor) 




# Single cycle check
   Given a list of integers, write a function that takes in that list and return
   a boolean that determine whether the list has a single cycle

   list = [2, 3, 1, -4, -4, -1]
   each integer represents the number of jumps in the array
   so 2 jumps twice to value 1. 1 jumps forward to value -4 and -4 jumps
   backwards four times and ends on value -1
   
   1. we want to make sure we visit n elements where n is the length of the list
   2. if we visit more than one element, and we find ourselves back at 
      the starting point which is 2, without visiting all elements in the list, we return
      False
   3. If we visit all element in the list, and we're not back at the starting
      point, return False
      
```py
def hasSingleCycle(_array):
   currentIndex = 0
   elementsVisited = 0
   while elementsVisited < len(_array):
      if elementsVisited > 0 and currentIndex == 0:
              return  False
   elementsVisited += 1
   currentIndex = getNextIndex(currentIndex,_array)
   return currentIndex == 0

def getNextIndex(currentIndex, array):
    jump = array[currentIndex]
    nextIndex = (currentIndex + jump) % len(array)
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)
    
        
```
      
# Frequency of an element and get rid of duplicates in a list
1. set initial **frequency** to **0**
2. keep track of all counted items in a hash table called **counted**
3. sort the list in ascending order.

       frequency = 0
       counted = {}

4. for each **num** in the list, if the **num** is in the **hash table**, increment
   frequency by 1
5. if not, set frequency to 1 
6. add the num to the hash table
   
# Dijkstra's Algorithm


# Sliding window maximum element of k values
E.g. nums = [1, 3, -1, -3, 5, 3, 6, 7], k=3
[1, 3, -1] = 3,
[3, -1, -3] = 3, 
[-1, -3, 5] = 5, 
[-3, 5, 3] = 5, 
[5, 3, 6] = 6,
[3, 6, 7] = 7
output: = [3, 3, 5, 5, 6, 7]

1. Our `function` will have two params, **nums** and **k** where nums represent
   our list and k represents our window size.
2. we will have an `output` variable to keep track of our max values
3. we will use a queue data structure to keep track of values in our window
4. Our sliding window will have both **left** and **right** pointers 
   where `l = 0, and r = 0`   
5. while our right pointer index is not more than the length of our list, while our 
   queue is not empty, and the left pointer value in our window is greater than the right,
   pop the first value off the queue. repeat the process till the condition is False.
6. Append the right pointer index into the queue
```py
def max():
   nums:list
   k: int
   output = [],Queue = [], l = r = 0
   while len(Queue) >= 1 and nums[Queue[-1]] < nums[r]:
      while len(Queue) >= 1 and nums[Queue[-1]] < nums[r]:
         Queue.pop(0)
      Queue.append(r)
      # remove left value from window
      if l > Queue[0]:
        Queue.pop(0)
      if (r + 1) >= k:
        output.append(nums[Queue[0]])
        l += 1
      r += 1
   return output 
```


# SELECTION SORT - using recursion
1. The base case is, if the list is empty or has only one
   item, return the list, else, start from point 2
2. Given a sequence of unsorted nums, create a list out of them 

        new_sequence = list(sequence_of_nums)

3. search for the index of the min value in the sequence
   and save it in a variable **min_index**
   
        min_index = new_sequence.index(min(new_sequence))

4. find the value of min_index and save it in a variable
   
        min_value = new_sequence[min_index]

5. swap the min_value with the first item in the list

        new_sequence[min_index] = new_sequence[0]
        new_sequence[0] = min_value

6. return a list of min_value + recursive call to the function
   starting from the second item in the list
   
        return [min_value] + select_sort_rec(b[1:])



# Kadane's Algorithm (Largest Sum Contiguous Subarray)
This finds the maximum sum of all possible subarrays 
Time = O(N), space = O(1)
        
1. set **currentMax** and **FinalMax** to first item in the array
         
       currentMax = FinalSum = array[0]

2. loop through the list keep track of **currentNum**
       
       for currentNum in array[1:]:
   
3. find max of (currentNum) and (currentNum + currentMax)

       currentMax = max(currentNum, currentMax + currentNum)

4. update the values of both currentMax and FinalMax
   
       finalMax = max(finalMax, currentMax)

[3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
E.g currentMaxSum = 3 picked -> 3+5 = 8 or 5, 8 picked -> 8 + -(9) = -1 or -9, -1 picked -> 
-1 + 1 = 0 or 1, 1 picked -> and so on,... 
    finalMax = 3 -> 8, ... -> 19 
    finalMax = 19
    


# Find path between two Nodes in a Graph
1. the function takes four parameters, **path, start(of the path), end, and a graph**
2. if the path is None, create it. 

       if path is None:
          path = []
       path = path + [start]
3. return path if start is the same as end, thus if path has only one item
   
       if start == end:
          return path
4. return None if a path cannot be found

       if graph.get(key) is None:
          return None
5. For a node in graph if a node is not in path, create a new_path and assign 
   the result of a recursive call of the function to it

       for node in self.graph[start]:
           if node not in path:
              new_path = find_path(path, start, end, graph)
              if new_path:
                  return new_path 





# Move instances of K elements to the end of the Array

      input = [2, 1, 2, 2, 2, 3, 4, 2], valueToMove = 2
      output = [1, 3, 4, 2, 2, 2, 2, 2]

1. initialize a left, right pointer, variable valueToMove
2. while left is less than right:
3. reduce the right pointer by 1 while left is less than right and right value is equal to valueToMove
4. move out of the second while loop and check If left value is equal to valueToMove, swap left and right values
5. while left is still less than right increment left pointer by one and return the array


```py
# O(N)T, O(1)S
def moveInstances(arr, k):
    # valueToMove = k
    left = 0
    right = len(arr) - 1
    while left < right:
       while left < right and arr[right] == k:
         right -= 1
       if arr[left] == k: # swap and right value
          arr[left], arr[right] = arr[right], arr[left]
       left += 1
    return arr
print(moveInstances([2, 1, 2, 2, 2, 3, 4, 2], 2))

OR

def move_to_left(arr, k):
    for item in arr:
        if item == k:
            arr.remove(item);
            arr.append(item);
    return arr
```





# Zigzag Traversal 
E.g. [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12,15],
    [7, 13, 14,16]
]
Output = [1, 2, 3, 4, ... , 15, 16]

1. Keep track of the directions, row, column, movingDown: bool, height and width
                 
         height = last row in our array
         width  = last col in our array
         row == height means we are at last row
         col == width means we are at last col

         row = col = 0,  movingDown = True, height = len(arr) - 1, width = len(arr[0]) - 1, newArray = [] 

2. we want to keep traversing our 2d array so far as we are not out of bounds
         
        while not outOfBounds(row, col, height, width):
            put current value in newArray
            if movingDown
               if At first_Column or last_Row 
                   movingDown = False
                   if last_Row(row == height)
                      increase col by 1
                   else   
                      increase row by 1
               else
                  reduce col by 1
                  increase row by 1
            else
               if at_First_Row or last_Column
                  movingDown = True
                  if last_Column(col == width) 
                     increase row by 1
                 else
                     increase col by 1
               else
                  increase col by 1  
                  reduce row by 1
        return newArray

3. create the outOfBounds function
      
       outOfBounds(row, col, height, row)
            return row < 0 or col < 0 or row > height or col > width



# QUICK SORT
1. Given an Array of integers, [8, 5, 2, 9, 5, 6, 3]
we're gonna chose the first element  as our pivot, p = 8
2. we're gonna initialize two pointers l, and r 
where l points to 5, and r points to 3.
3. while r >= l, continue to loop
4. while looping, if the l > p and r < p:
5. we'll swap the l and r, if Yes
6. if l is not > or = p, we'll increase l by 1
7. if r is not < p, we'll decrease r by 1
8. while l and r overlap, we'll swap p with final position of r
9. We'll repeat the iteration again
10. leftSubarrayIsSmaller = (length of the left subarray)r - 1 - s < e - r + 1(length of the right subarray)
11. O(n log n)T and O(log n )S





# SUBSTRING WITH CONCATENATION OF ALL WORDS

You are given a string `s` and an array of strings `words` of 
the same length. Return all starting indices of substring(s) 
in `s` that is a concatenation of each `word` in words exactly once, 
in any order, and without any intervening characters. 
You can return the answer in any order.

`Example 1:`

Input: s = “barfoothefoobarman”, 
words = [“foo”,“bar”]
Output: [0,9]
`
Example 2:
`
Input: s = “wordgoodgoodgoodbestword”,
words = [“word”,“good”,“best”,“word”] 
Output: []
`
Example 3:
`
Input: s = “barfoofoobarthefoobarman”, 
words = [“bar”,“foo”,“the”] 
Output: [6,9,12]

* ALGORITHM
1. create an empty list for the output
       `char_Idx = []`
2. concatenate the list of words and find its length
      `lenOfWords = len("".join(words))`
3. loop thru `words` and find n ways to arrange `words` in string `s`
      `for i in range((len(s)-lenOfWords)+1)`
   * During looping, determine whether we can find 
     words="barfoothe" represented differently in string, `s` in order to
     find anagrams of words eg. "barfoothe", "foobarthe", "thebarfoo",
     "foothebar"
       `possible_anagrams = s[i:i+lenOfWords]`
   * keep track of the length of a word in our list of 
     words = [“bar”,“foo”,“the”] 
        `n= len(words[0])`






