# O(N) T and S
def reverseWordsInString(string):
    words = [];
    startOFword = 0;
    # for index in range(len(string)):
        character = string[index];
        
        # adding word in a string when we hit a whitespace
        if character == " ":
            words.append(string[startOFword:index]);
            startOFword = index;

        # adding whitespaces to our list as well
        elif string[startOFword] == " ":
            words.append(" ");
            startOFword = index;

    words.append(string[startOFword:]);

    reverseList(words);
    return "".join(words);

# reverse words in the list
def reverseList(list):
    start, end = 0, len(list) - 1;
    while start < end:
        list[start], list[end] = list[end], list[start];
        start += 1;
        end -= 1;

print(reverseWordsInString("Hello Heavenly Father, I trust your works"));

print()