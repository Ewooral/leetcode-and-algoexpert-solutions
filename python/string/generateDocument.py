print(".....APPROACH I......")
# APPROACH I

# O(d * (c + d)) Time and O(1) space
def generate_document(characters, document):
    for character in document:
        documentFrequecy = countCharacterFrequency(character, document)
        charactersFrequecy = countCharacterFrequency(character, characters)
        # print(documentFrequecy, charactersFrequecy)
        if documentFrequecy > charactersFrequecy:
            return False
    
    return True

def countCharacterFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency


print(generate_document("alkdka;kj fkls akjdfie jaa;goina;sdfasilk", "in is life"))
print(generate_document("goaehalsng", "elangaa"))


print("..................")
"""

To generate a document out of a string,

1. Two identifiers/variables: characters, document.
2. Loop thru the document and save every character in a character variable 
3. At each character in the document, find the frequency of the character
in both the document and characters variables/identifiers
4. if document Frequency > characters frequency, return False, 
5. return True if everything pans out successfully

n = character string
m = document string
c = a character in both strings


"""
# O(m * (n + m)) Time | O(1) S


def genDoc(char: str, doc: str) -> bool:
    for c in doc:
        fC: int = FC(c, char)
        fD: int = FC(c, doc)
        # print(fC, fD)

        if fD > fC:
            return False
    return True


def FC(char, target) -> int:
    frequency = 0
    for c in target:
        if c == char:
            frequency += 1
    return frequency


print(genDoc("goaehalsng", "elangaa"))
print(genDoc("alkdka;kj fkls akjdfie jaa;goina;sdfasilk", "in is life"))



print(".......APPROACH II.........")
# APPROACH II
# O(c * (n + m)) time | O(c) space
def genDoc(char: str, doc: str):
    already_counted = set()

    for c in doc:
        if c in already_counted:
            continue
        fC = FC(c, char)
        fD = FC(c, doc)
        # print(fC, fD)

        if fD > fC:
            return False
        already_counted.add(c)
    return True


def FC(char, target):
    frequency = 0
    for c in target:
        if c == char:
            frequency += 1
    return frequency


print(genDoc("goaehalsng", "elangaa"))
print(genDoc("alkdka;kj fkls akjdfie jaa;goina;sdfasilk", "in is life"))




print("........APPROACH III........")
# APPROACH III
# O(n + m) time | O(c) space

def genDoc(chars, docs):
    c_Counts = {}

    for c in chars:
        if c not in c_Counts:
            c_Counts[c] = 0

        c_Counts[c] += 1

    for c in docs:
        if c not in c_Counts or c_Counts[c] == 0:
            return False
        c_Counts[c] -= 1
    return True


print(genDoc("goa ehalsng", "el angah"))
print(genDoc("alkdka;kj fkls akjdfie jaa;goina;sdfasilk", "in is life"))
