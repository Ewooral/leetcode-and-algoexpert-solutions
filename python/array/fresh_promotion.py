"""
Amazon is running a promotion in which customers receive prizes 
for purchasing a secret 
combination of fruits. The combination will change each day, 
and the team running the promotion wants to use a code list to make 
it easy to change the combination. The code list contains groups of 
fruits. Both the order of the groups within the code list and the order 
of the fruits within the groups matter. However, between the groups of 
fruits, any number, and type of fruit is allowable. The term "anything" is 
used to allow for any type of fruit to appear in that location within the 
group. 
Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the 
following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana

Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific 
fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output
Return an integer 1 if the customer is a winner else return 0.

Note
'anything' in the codeList represents that any fruit can be 
ordered in place of 'anything' in the group. 'anything' has to be something, 
it cannot be "nothing." 'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: codeList = [[apple, apple], [banana, anything, banana]] 
shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of
'anything' in the shoppingCart. The customer is a winner as the customer
has added fruits in the order of fruits in the groups and the order 
of groups in the codeList is also maintained in the shoppingCart.

Example 2:
Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]

Output: 0
Explanation:
The customer is not a winner as the customer has added 
the fruits in order of groups but group [banana, orange, banana] 
is not following the group [apple, apple] in the codeList.

Example 3:

Input: codeList = [[apple, apple], [banana, anything, banana]] 
shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0
Explanation:
The customer is not a winner as the customer has added the 
fruits in an order which is not following the order of fruit
names in the first group.

Example 4:

Input: codeList = [[apple, apple], [apple, apple, banana]] 
shoppingCart = [apple, apple, apple, banana]
Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, 
all three fruits would form group 2, but can't because it would 
contain all fruits of group 1.


==========JAVA CODE=========

 private static int freshPromotion(String[][] codeList, String[] shoppingCart) {
//        Start at 0 index for both the code list and shopping cart.
        int cartIdx = 0, codeIdx = 0;
        while (cartIdx < shoppingCart.length && codeIdx < codeList.length) {
            String cur = shoppingCart[cartIdx];
//            If the first fruit of the codeList is anything or if it matches the current fruit at the cart idx.
            if((codeList[codeIdx][0].equals("anything") || codeList[codeIdx][0].equals(cur)) && hasOrder(shoppingCart, cartIdx, codeList[codeIdx])){
                cartIdx += codeList[codeIdx++].length;
            }else{
                cartIdx++;
            }
        }
//        If the all the codeList is present then return 1, else 0.
        return codeIdx == codeList.length ? 1 : 0;
    }

    private static boolean hasOrder(String[] shoppingCart, int idx, String[] order) {
//        Loop through the codeList to check if the fruits are in order.
        for (String s : order) {
            if (idx < shoppingCart.length && (s.equals("anything") || shoppingCart[idx].equals(s))){
                idx++;
            }else{
                return false;
            }
        }
        return true;
    }


=======Python regex solution:===========

def freshPromotion(shoppingCart, codeList) -> int:
    s = ' '.join(shoppingCart)
    print(s)
    reg = ''
    for code in codeList:
        c = ' '.join(code)
        c = ' ' + c
        c = c.replace('anything', '\w+')
        reg += c + '[\w\s]*'
    r = re.compile(reg)
    res = r.findall(s)
    return min(1, len(res))




========= JAVA CODES ================ 

public class FreshPromotion {

	  public static int foo(List<String> codeList, List<String> shoppingCart) {
		Stack<String> orderStack = new Stack<>();
		Stack<Stack<String>> codeStack = new Stack<>();
		boolean isFound = false;
		String orderFruit = "";
		String prevCodeFruit = "";

		if (codeList.isEmpty()) {
		  return 1;
		}

		pushCodeStack(codeList, codeStack);
		pushOrderStack(shoppingCart, orderStack);

		while (!codeStack.isEmpty()) {
		  Stack<String> codeFruitStack = codeStack.pop();
		  isFound = false;
		  while (!codeFruitStack.isEmpty()) {
			String codeFruit = codeFruitStack.pop();
			if (orderStack.isEmpty()) {
			  return 0;
			}

			if (isFound) {
			  orderFruit = orderStack.pop();

			  if (!checkFruit(codeFruit, orderFruit)) {
				isFound = false;
				codeFruitStack.push(prevCodeFruit);
			  }
			}

			while (!isFound && !orderStack.isEmpty()) {
			  orderFruit = orderStack.pop();
			  if (checkFruit(codeFruit, orderFruit)) {
				isFound = true;
			  }
			}

			prevCodeFruit = codeFruit;
		  }
		}

		if (!isFound && orderStack.isEmpty()) {
		  return 0;
		}

		return 1;
	  }

	  private static void pushOrderStack(List<String> shoppingCart, Stack<String> orderStack) {
		for (int j = shoppingCart.size() - 1; j >= 0; j--) {
		  orderStack.push(shoppingCart.get(j));
		}
	  }

	  private static void pushCodeStack(List<String> codeList, Stack<Stack<String>> codeStack) {
		for (int j = codeList.size() - 1; j >= 0; j--) {
		  Stack<String> stringStack = new Stack<>();
		  String code = codeList.get(j);
		  String[] codeFruits = code.split(" ");

		  for (int i = codeFruits.length - 1; i >= 0; i--) {
			stringStack.push(codeFruits[i]);
		  }
		  codeStack.push(stringStack);
		}
	  }

	  private static boolean checkFruit(String codeFruit, String orderFruit) {
		if (codeFruit.equalsIgnoreCase("anything")) {
		  return true;
		} else if (codeFruit.equalsIgnoreCase(orderFruit)) {
		  return true;
		} else {
		  return false;
		}
	  }

	}



==========JAVASCRIPT ===============

function foo(codeList, shoppingCart) {
    // Write your code here
    let listIndex = 0;
    let ret = 0;
    let itemInListIndex = 0;
    const numberOfCodeLists = codeList.length;
    shoppingCart.forEach(shoppingCartItem => {
        const currList = codeList[listIndex].split(' ');
        const secretListCurrItem = currList[itemInListIndex];
        if (secretListCurrItem === shoppingCartItem ||
            secretListCurrItem === 'anything') 
        {
            itemInListIndex++;

            if (itemInListIndex === currList.length) {
                itemInListIndex = 0;
                listIndex++;
                if (listIndex === numberOfCodeLists) {
                    ret = 1;
                    return;
                }
            }
        }
        else {
            itemInListIndex = 0;
        }
    });

    return ret;
}


========== PYTHONPATH ====================== 

Python solution using two pointers

# N: # of codeList
# M: # of items in shopping cart

# Time complexity: O(M)
# Space complexity : O(1)
def freshPromotion(codeList, shoppingCart):
    matched = 0
    cartIndex = 0
    for code in codeList:
        found = False
        while cartIndex < len(shoppingCart):
            if shoppingCart[cartIndex] != code[0] and shoppingCart[cartIndex] is not 'anything':
                cartIndex += 1
                continue
            cartIndex += 1
            codeIndex = 1
            while codeIndex < len(code) and cartIndex < len(shoppingCart):
                if code[codeIndex] != shoppingCart[cartIndex] \
                        and code[codeIndex] is not 'anything':
                    break
                codeIndex += 1
                cartIndex += 1
            if codeIndex == len(code):
                found = True
                break
        if found:
            matched += 1
        if cartIndex == len(shoppingCart):
            break
    return matched == len(codeList)

TESTING

if __name__ == '__main__':
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple', 'apple'], ['banana', 'apple', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['banana', 'orange', 'banana', 'apple', 'apple']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'apple', 'apple', 'banana']) \
           == False
"""


def fresh_promotion(code_list, shopping_cart):
    matched = 0
    cart_index = 0
    for code in code_list:
        found = False
        while cart_index < len(shopping_cart):
            if shopping_cart[cart_index] != code[0] and shopping_cart[cart_index]!= 'anything':
                cart_index += 1
                continue
            cart_index += 1
            code_index = 1
            while code_index < len(code) and cart_index < len(shopping_cart):
                if code[code_index] != shopping_cart[cart_index] \
                        and code[code_index] != 'anything':
                    break
                code_index += 1
                cart_index += 1
            if code_index == len(code):
                found = True
                break
        if found:
            matched += 1
        if cart_index == len(shopping_cart):
            break
    return matched == len(code_list)


if __name__ == '__main__':
    assert fresh_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
        == True
    assert fresh_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
        == True
    assert fresh_promotion([['orange', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
        == True
    assert fresh_promotion([['orange', 'apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \

            
print( fresh_promotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                             ['orange', 'apple', 'apple', 'banana', 'orange', 'banana'])
      == True)



# ANOTHER SOLUTION
def is_winner(secret, order):
    if not secret:
        return True
    i = k = 0
    while i < len(secret):
        group = secret[i]
        j = 0
        while j < len(group):
            if k == len(order):
                return False
            if group[j] == 'anything' or group[j] == order[k]:
                k += 1
                j += 1
            else:
                # pushing k back to (assumed start position of group ) + 1
                k -= j - 1
                j = 0
        i += 1
    return True
