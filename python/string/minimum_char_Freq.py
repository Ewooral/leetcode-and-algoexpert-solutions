# O(n * l) time | O(c) s

def min_char_word(words):
  maxCharFreq = {}
  for word in words:
    charFreq1 = freq(word)
    updateMaxFreq(charFreq1, maxCharFreq)
  return makeArrayFromCharFreq(maxCharFreq)


def countCharFreq(string):
  charFreqs = {}
  for char in string:
    if char not in charFreqs:
      charFreqs[char] = 0
    charFreqs[char] += 1
  return charFreqs


def freq(li):
  dic = {}
  for n in li:
    dic[n] = dic.get(n, 0) + 1
  return dic


def updateMaxFreq(freqs, maxFreqs):
  for char in freqs:
    freq = freqs[char]
    if char in maxFreqs:
      maxFreqs[char] = max(freq, maxFreqs[char])
    else:
      maxFreqs[char] = freq


def makeArrayFromCharFreq(charFreqs1):
  chars = []
  for char in charFreqs1:
    freq = charFreqs1[char]
    for _ in range(freq):
      chars.append(char)
  return chars


print(min_char_word(["this", "that", "did", "deed", "them" "a"]))
