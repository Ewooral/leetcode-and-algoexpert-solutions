def select_sort_rec(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        min_index = b.index(min(b))
        aux = b[min_index]
        # aux = b[min_index]
        b[min_index] = b[0]
        b[0] = aux
        # b[0] = aux

    return [aux] + select_sort_rec(b[1:])


print(select_sort_rec([3, 0, 9, 1, 5, 4]))


def select_sort_recAA(a):
    print("selection_sort ", "(", a, ")")
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        mini = min(b)
        b.remove(mini)

    return [mini] + select_sort_rec(b)


print(select_sort_recAA([3, 2, 6, 0, 1, 10]))
