/**
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D
 * and M.
 * 
 * Symbol Value
 * I = 1
 * V = 5
 * X = 10
 * L = 50
 * C = 100
 * D = 500
 * M = 1000
 * For example, 2 is written as II in Roman numeral, just two one's added
 * together. 12 is written as XII, which is simply X + II. The number 27 is
 * written as XXVII, which is XX + V + II.
 * 
 * Roman numerals are usually written largest to smallest from left to right.
 * However, the numeral for four is not IIII. Instead, the number four is
 * written as IV. Because the one is before the five we subtract it making four.
 * The same principle applies to the number nine, which is written as IX. There
 * are six instances where subtraction is used:
 * 
 * I can be placed before V (5) and X (10) to make 4 and 9.
 * X can be placed before L (50) and C (100) to make 40 and 90.
 * C can be placed before D (500) and M (1000) to make 400 and 900.
 * Given an integer, convert it to a roman numeral.
 * 
 * 
 * 
 * Example 1:
 * 
 * Input: num = 3
 * Output: "III"
 * Explanation: 3 is represented as 3 ones.
 * Example 2:
 * 
 * Input: num = 58
 * Output: "LVIII"
 * Explanation: L = 50, V = 5, III = 3.
 * Example 3:
 * 
 * Input: num = 1994
 * Output: "MCMXCIV"
 * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 * 
 * 
 * Constraints:
 * 
 * 1 <= num <= 3999
 * 
 */



 // Approach 1:
 /**
  * Time complexity : O(1).
  * 
  * As there is a finite set of roman numerals, there is a hard upper limit on
  * how many times the loop can iterate. This upper limit is 15 times, and it
  * occurs for the number 3888, which has a representation of MMMDCCCLXXXVIII.
  * Therefore, we say the time complexity is constant, i.e. O(1).
  * 
  * Space complexity : O(1).
  * 
  * The amount of memory used does not change with the size of the input integer,
  * and is therefore constant.
  */

 class Solution {
     private static final int[] values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
     private static final String[] symbols = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };

     public String intToRoman(int num) {
         StringBuilder sb = new StringBuilder();
         // Loop through each symbol, stopping if num becomes 0.
         for (int i = 0; i < values.length && num > 0; i++) {
             // Repeat while the current symbol still fits into num.
             while (values[i] <= num) {
                 num -= values[i];
                 sb.append(symbols[i]);
             }
         }
         return sb.toString();
     }
 }

 /**
  * Approach 1: Greedy
  * Intuition
  * 
  * Representing a given integer as a Roman Numeral requires finding a sequence
  * of the above 13 symbols, where their corresponding values add up to the
  * integer. This sequence must be in order from largest to smallest, based on
  * symbol value. To remind you, these are the symbol values.
  * 
  * Symbol mapping
  * 
  * As explained in the overview, the representation should use the largest
  * possible symbols, working from the left. Therefore, it makes sense to use a
  * Greedy algorithm. A Greedy algorithm is an algorithm that makes the best
  * possible decision at the current time; in this case taking out the largest
  * possible symbol it can.
  * 
  * So to represent a given integer, we look for the largest symbol that fits
  * into it. We subtract that, and then look for the largest symbol that fits
  * into the remainder, and so on until the remainder is 0. Each of the symbols
  * we take out are appended onto the output Roman Numeral string.
  * 
  * For example, suppose we need to make the number 671.
  * 
  * The largest symbol that fits into 671 is D (which is worth 500). The next
  * symbol up, CM, is worth 900 and so is too big to fit. Therefore, we now have
  * the following.
  * 
  * Roman Numeral so far: D
  * Integer remainder: 671 - 500 = 171
  * We now repeat the process with 171. The largest symbol that fits into it is C
  * (worth 100).
  * 
  * Roman Numeral so far: DC
  * Integer remainder: 171 - 100 = 71
  * Repeating this with 71, we find the largest symbol that fits in is L (worth
  * 50).
  * 
  * Roman Numeral so far: DCL
  * Integer remainder: 71 - 50 = 21
  * For 21, the largest symbol that fits in is X (worth 10).
  * 
  * Roman Numeral so far: DCLX
  * Integer remainder: 21 - 10 = 11
  * For 11, the largest symbol that fits in is again X.
  * 
  * Roman Numeral so far: DCLXX
  * Integer remainder: 11 - 10 = 1
  * Finally, the 1 is represented with a I and we're done.
  * 
  * Roman Numeral so far: DCLXXI
  * Integer remainder: 1 - 1 = 0
  * In pseudocode, this algorithm is as follows.
  * 
  * define function to_roman(integer):
  * roman_numeral = ""
  * while integer is non-zero:
  * symbol = biggest valued symbol that fits into integer
  * roman_numeral = concat roman_numeral and symbol
  * integer = integer - value of symbol
  * return roman_numeral
  * The cleanest way to implement this in code is to loop over each symbol, from
  * largest to smallest, checking how many copies of the current symbol fit into
  * the remaining integer.
  * 
  * define function to_roman(integer):
  * roman_numeral = ""
  * for each symbol from largest to smallest:
  * if value of symbol is greater than integer:
  * continue
  * symbol_count = number of times symbol value fits into integer
  * repeat symbol_count times:
  * roman_numeral = concat roman_numeral and symbol
  * integer = integer - (value of symbol * symbol_count)
  * 
  * return roman_numeral
  * Here's an animation showing this algorithm run on the number 478.
  * 
  * 
  */


// APPROACH 2

  class IntegerToRoman {
     private static final String[] thousands = { "", "M", "MM", "MMM" };
     private static final String[] hundreds = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
     private static final String[] tens = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
     private static final String[] ones = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };

     public String intToRoman(int num) {
         return thousands[num / 1000] + hundreds[num % 1000 / 100] + tens[num % 100 / 10] + ones[num % 10];
     }
 }

 /**
  * Complexity Analysis
  * 
  * Time complexity : O(1)O(1).
  * 
  * The same number of operations is done, regardless of the size of the input.
  * Therefore, the time complexity is constant.
  * 
  * Space complexity : O(1)O(1).
  * 
  * While we have Arrays, they are the same size, regardless of the size of the
  * input. Therefore, they are constant for the purpose of space-complexity
  * analysis.
  * 
  * The downside of this approach is that it is inflexible if Roman Numerals were
  * to be extended (which is an interesting follow-up question). For example,
  * what if we said the symbol H now represents 5000, and P now represents 10000,
  * allowing us to represent numbers up to 39999? Approach 1 will be a lot
  * quicker to modify, as you simply need to add these 2 values to the code
  * without doing any calculations. But for Approach 2, you'll need to calculate
  * and hardcode ten new representations. What if we then added symbols to be
  * able to go up to 399,999,999? Approach 2 becomes more and more difficult to
  * manage, the more symbols we add.
  */
