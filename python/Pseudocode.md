## REVERSE WORDS IN STRINGS .....................................

1. inputs: 
        
            words = "good god is alive"
            startOfword = 0
            reverse_word = []
        
    - loop through the input string and keep track of the start of the each character. Assume the start of word = 0.

            for index in range(len(words)):
                ......

2. Convert the string to a list

    - When looping, if you encounter a whitespace " ", append from the start of the string to the current string (words[startOfword:index])
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

3. return True if stack is empty and False if not empty
        
        return len(stack) == 0. 




# Breadth First Search Algorithm.........................

1. keep a **QUEUE** data structure containing list of vertices and adjacent edges thru which you want to search for a particular item.

2. dequeue a vertex off the queue and check if it matches with what you're looking for

3. if yes, mark the vertex or edge as checked and then return True

4. if no, check if vertex has neighbors or adjacent vertices and enqueue them in the queue

5. dequeue the next item off the queue and repeat the process again until the queue is empty while marking each item as checked!

6. return False if nothing is found



# Depth First Search Algorithm.............................

1. keep a **STACK** data structure containing list of vertices and adjacent edges thru which you want to search for a particular item.

2. dequeue a vertex off the queue and check if it matches with what you're looking for

3. if yes, mark the vertex or edge as checked and then return True

4. if no, check if vertex has neighbors or adjacent vertices and enqueue them in the queue

5. dequeue the next item off the queue and repeat the process again until the queue is empty while marking each item as checked!

6. return False if nothing is found


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
        def hasSingleCycle(array):
        currentIndex = 0
        elementsVisited = 0
        while elementsVisited < len(array):
        if elementsVisited > 0 and currentIndex == 0:
                return  False
        elementsVisited += 1
        currentIndex = getNextIndex(currentIndex, array)
        return currentIndex == 0

        def getNextIndex(currentIndex, array):
        jump = array[currentIndex]
        nextIndex = (currentIndex + jump) % len(array)
        return nextIndex if nextIndex >= 0 else nextIndex + len(array)
            
        
   ```
      

   