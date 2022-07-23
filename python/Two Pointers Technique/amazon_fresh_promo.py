from typing import List


def freshPromotion(codeList: List, shoppingCart: List):
    # check for edge cases
    if codeList is None or len(codeList) == 0:
        return 1
    if shoppingCart is None or len(shoppingCart) == 0:
        return 0
    clIdx = scIdx = 0
    while clIdx < len(codeList) and scIdx + len(codeList[clIdx]) <= len(shoppingCart):
        match: bool = True
        for itemIdx in range(len(codeList[clIdx])):
            if not codeList[clIdx][itemIdx] == "anything" and not shoppingCart[itemIdx + scIdx] == codeList[clIdx][
                itemIdx]:
                match = False
                break
        if match:
            scIdx += len(codeList[clIdx])
            clIdx += 1
        else:
            scIdx += 1
    # return clIdx == len(codeList) if 1 else 0
    return 1 if clIdx == len(codeList) else 0


def main():
    codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart = ["orange", "apple", "apple", "banana", "anything", "banana"]

    codeList1 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart1 = ["banana", "orange", "banana", "apple", "apple"]

    codeList2 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart2 = ["apple", "banana", "apple", "banana", "orange", "banana"]

    codeList3 = [["apple", "apple"], ["banana", "anything", "banana"]]
    shoppingCart3 = ["apple", "banana", "apple", "banana", "orange", "banana"]

    codeList4 = [["apple", "apple"], ["apple", "apple", "banana"]]
    shoppingCart4 = ["apple"]

    print("Note that 0, 1 represent False and True respectively")
    print(freshPromotion(codeList, shoppingCart))
    print(freshPromotion(codeList1, shoppingCart1))
    print(freshPromotion(codeList2, shoppingCart2))
    print(freshPromotion(codeList3, shoppingCart3))
    print(freshPromotion(codeList4, shoppingCart4))


if __name__ == '__main__':
    main()
