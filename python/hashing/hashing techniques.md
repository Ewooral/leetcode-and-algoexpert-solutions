# Hashing is a searching technique

    We already know there are two types of searching techniques
        1. Linear O(n)
        2. Binary Search O(log n). Binary search is only effective if 
        extra effort is made by sorting the list or array.

        3. Hashing is also a searching Technique.
  
hashes are good for
    
    • Modeling relationships from one thing to another thing
    • Filtering out duplicates
    • Caching/memorizing data instead of making your server do work
 
 ## hash table usecases
    Suppose you want to build a phone book like this. You’re mapping 
  people’s names to phone numbers. Your phone book needs to have this 
  functionality:

    • Add a person’s name and the phone number associated 
    with that person.
    • Enter a person’s name, and get the phone number associated 
    with that name.
    This is a perfect use case for hash tables! Hash tables are 
    great when you want to
    • Create a mapping from one thing to another thing
    • Look something up
  Building a phone book is pretty easy. First, make a new hash table:
  >>> phone_book = dict()

    By the way, Python has a shortcut for making a new hash table. You can 

  use two curly braces:
  >>> phone_book = {} Same as phone_book = dict()

    Let’s add the phone numbers of some people into this phone book:

  >>> phone_book[“jenny”] = 8675309
  >>> phone_book[“emergency”] = 911

    That’s all there is to it! Now, suppose you want to find 
    Jenny’s phone number. Just pass the key in to the hash:

  >>> print phone_book[“jenny”]
  8675309 Jenny’s phone number

## The drawback for hashing is space problem

* Hashing use two mapping functions

      keys (8, 3, 6, 10, 15, 9, 4)

      1. one to one. (Ideal Hash function) 
        => h(x) = x
           
        The draw back is that, the space needed is huge. Huge space could
        be resolved using the modulus hashing technique

      2. many to one (Modulus Hash function)
        => h(x) = x % len(arr)

        The draw back is that collision may be achieved

* Two methods used to solve collision problem

      1. Open Hashing
        - Chaining
          With chaining, if there is a collision, the keys are chained using a linked list in a sorting order

      2. closed Hashing
        - linear probing
        - quadratic probiing 
        - double probing


# Properties of a good Hash function
1. It distributes hash values uniformly across hash tables

2. It has to use all the input data

# Collision Resolution Techniques
  To avoid collisions, you need
  
    • A low load factor
    • A good hash function

    load factor = (no of items in the list or array) / len(list or array)

# Uses of a hash table

• You can make a hash table by combining a hash function 
with an array.
• Collisions are bad. You need a hash function that 
minimizes collisions.
• Hash tables have really fast search, insert, and delete.
• Hash tables are good for modeling relationships from one 
item to another item.
• Once your load factor is greater than .07, it’s time to resize 
your hash table.
• Hash tables are used for caching data (for example, with 
a web server).
• Hash tables are great for catching duplicates