""" 
Approach 1: Greedy
Intuition

Representing a given integer as a Roman Numeral requires finding a sequence of the above 13 symbols, where their corresponding values add up to the integer. This sequence must be in order from largest to smallest, based on symbol value. To remind you, these are the symbol values.

Symbol mapping

As explained in the overview, the representation should use the largest possible symbols, working from the left. Therefore, it makes sense to use a Greedy algorithm. A Greedy algorithm is an algorithm that makes the best possible decision at the current time; in this case taking out the largest possible symbol it can.

So to represent a given integer, we look for the largest symbol that fits into it. We subtract that, and then look for the largest symbol that fits into the remainder, and so on until the remainder is 0. Each of the symbols we take out are appended onto the output Roman Numeral string.

For example, suppose we need to make the number 671.

The largest symbol that fits into 671 is D (which is worth 500). The next symbol up, CM, is worth 900 and so is too big to fit. Therefore, we now have the following.

Roman Numeral so far: D
Integer remainder: 671 - 500 = 171
We now repeat the process with 171. The largest symbol that fits into it is C (worth 100).

Roman Numeral so far: DC
Integer remainder: 171 - 100 = 71
Repeating this with 71, we find the largest symbol that fits in is L (worth 50).

Roman Numeral so far: DCL
Integer remainder: 71 - 50 = 21
For 21, the largest symbol that fits in is X (worth 10).

Roman Numeral so far: DCLX
Integer remainder: 21 - 10 = 11
For 11, the largest symbol that fits in is again X.

Roman Numeral so far: DCLXX
Integer remainder: 11 - 10 = 1
Finally, the 1 is represented with a I and we're done.

Roman Numeral so far: DCLXXI
Integer remainder: 1 - 1 = 0
"""

# APPROACH 1 
# T = O(1)
# S = O(1)

class SolutionI:
    def int_to_roman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                  (5, "V"), (4, "IV"), (1, "I")]

        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:

            # We don't want to continue looping if we're done.
            if num == 0:
                break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)

roman_numerals = SolutionI()
print(roman_numerals.int_to_roman(2333))



# Approach 2: 
# T = O(1)
# S = O(1)

class SolutionII:
    def int_to_roman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (thousands[num // 1000] + hundreds[num % 1000 // 100]
                + tens[num % 100 // 10] + ones[num % 10])
