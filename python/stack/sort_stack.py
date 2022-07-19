# O(n^2) time | O(n) space
def sort_stack(stack):
    if len(stack) == 0:
        return stack
    top = stack.pop()
    sort_stack(stack)
    insert_in_sorted_order(stack, top)
    return stack


def insert_in_sorted_order(stack, value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    top = stack.pop()
    insert_in_sorted_order(stack, value)
    stack.append(top)


print(sort_stack([1, 3, 4, -2, 2, -5]))
