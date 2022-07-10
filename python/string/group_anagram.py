'''
Given a list of words or arbitrary strings, write a function to
return a list of other list, where each of the other lists is a
group of anagrams

Input: [go, act, blop, tac, cat, og, olbp]
ouput: [[yo, oy], [blop, olpb], [act, tac, cat]]

solution
   0   1   2      3     4   5   6
  [go, act, blop, tac, cat, og, olbp]

# sort characters in string
-> oy, act, blop, act, act, og, blop

#

'''
# O(w * n * log n + n * w * log(w)) T, O(wn)

# APPROACH 1
def group_anagram(words):
    if len(words) == 0:
        return []
    sorted_words = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sorted_words[x])

    result = []
    current_anagram_group = []
    current_anagram = sorted_words[indices[0]]
    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if sorted_word == current_anagram:
            current_anagram_group.append(word)
            continue
        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word
    result.append(current_anagram_group)
    return result


# APPROACH 2
# O(w * n * log n) t | o(wn) s
def groupAnagram(words):
    anagrams = {}
    for word in words:
        sorted_words = "".join(sorted(word))
        if sorted_words in anagrams:
            anagrams[sorted_words].append(word)
        else:
            anagrams[sorted_words] = [word]
    return list(anagrams.values())


def main():
    b = ["go", "og", "act", "cat"]
    print(group_anagram(b))
    print(groupAnagram(b))


if __name__ == '__main__':
    main()