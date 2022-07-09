# O(N^2)T, O(1)S
def first_non_repeating_char(string):
    found_duplicate = False
    for ch in range(len(string)):
        for ch2 in range(len(string)):
            if string[ch] == string[ch2] and ch != ch2:
                found_duplicate = True
        if not found_duplicate:
            return string[ch]
    return -1


print(first_non_repeating_char("abcdfd"))


# O(N)T, O(1)S
def FirstNonRepeatingChar(Str):
    freq = {}
    for ch in Str:
        freq[ch] = freq.get(ch, 0) + 1
    for i in range(len(Str)):
        ch2 = Str[i]
        if freq[ch2] == 1:
            return ch2
    return -1


print(first_non_repeating_char("abcdf"))
