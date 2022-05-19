# HASH FUNCTIONS
# 1. Mod function

def mod(number, array_length):
    return number % array_length

print(mod(700, 24))


# 2. Ascii function

def modASCII(string, array_length):
    total = 0
    for i in string:
        total += ord(i)
    return total % array_length

print(modASCII("ABC", 24)) 