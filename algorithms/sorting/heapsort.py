from ds.heap.heap import heapify
from ds.heap.heap import heappop


def sort(lst):
    lst = lst[:]
    ret = []
    heapify(lst)
    while True:
        if len(lst) == 0:
            return ret
        ret.append(heappop(lst))
