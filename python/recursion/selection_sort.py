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
