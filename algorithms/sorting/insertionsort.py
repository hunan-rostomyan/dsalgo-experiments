def extract_min(lst):
    """Extracts the min from given list, returning
    the element and the list without it."""
    assert len(lst) >= 1

    min_i = 0
    i = 0
    while i < len(lst):
        if lst[i] < lst[min_i]:
            min_i = i
        i += 1

    newLst = lst[:min_i] + lst[min_i + 1:]
    return lst[min_i], newLst


def sort(lst):
    ret = []
    while True:
        if len(lst) == 0:
            return ret
        smallest, lst = extract_min(lst)
        ret.append(smallest)


def sort_rec(lst):
    """Recursive iteration version for fun"""
    def aux(sofar, lst):
        if len(lst) == 0:
            return sofar
        smallest, lst = extract_min(lst)
        return aux(sofar + [smallest], lst)
    return aux([], lst)
