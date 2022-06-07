# two sum 
'''
array = [2, 5, 1, -1, 4, 3, 0]
target = 3

a + b = target
a = currentValue
b = nextValue

hash_t = {
    3 - 2=1: "Added",
    3 - 5=-2: "Added",
    3 - 1=2: "Added",
    3 -(-1)=4: "Added",
    3 - 4=-1: "not added",
    
    .
    .
    3 - 0: "Added",

}

'''


def two_sum(clist: list, target: int) -> list:
    hash_table = {}
    for value in clist:
        nextValue = target - value
        if nextValue in hash_table:
            print([value, nextValue])
        else:
            hash_table[value] = "Added"
    print(hash_table)
    return []




'''
[1, 3, 9, 1, 0]
'''

def has_duplicate(clist: list) -> bool:
    pass

def main() -> None:
    two_sum([2, 5, 1, -1, 4, 3, 0], 3)

    if __name__ == "__main__":
        main()
