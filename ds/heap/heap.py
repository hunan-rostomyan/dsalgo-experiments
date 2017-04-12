from math import floor


# TODO: can we use None instead?
def parent(i):
    if i == 0:
        return -1
    else:
        return floor((i - 1) / 2)


def children(i, ceil):
    left_i = (i * 2) + 1
    right_i = (i * 2) + 2

    if left_i > ceil:
        left_i = None

    if right_i > ceil:
        right_i = None

    return left_i, right_i


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def heappush(heap, item):
    heap.append(item)
    i = len(heap) - 1
    while i >= 0:
        p = parent(i)
        if p == -1 or heap[p] <= heap[i]:
            return
        swap(heap, p, i)
        i = p


def heapify(items):
    # Build a heap
    heap = []
    for item in items:
        heappush(heap, item)

    # Copy heap to items
    for i, _item in enumerate(items):
        items[i] = heap[i]


def bubble_down_from(heap, i, last_i):
    while i <= last_i:
        cur = heap[i]
        left_i, right_i = children(i, last_i)
        min_i = left_i or right_i

        if not min_i:
            return

        if left_i and right_i:
            min_i = left_i if heap[left_i] <= heap[right_i] else right_i

        if min_i and heap[min_i] < cur:
            swap(heap, i, min_i)

        i = min_i


def heappop(heap):
    if not heap:
        return

    item = heap[0]
    last_i = len(heap) - 1
    heap[0] = heap[last_i]
    del heap[last_i]

    bubble_down_from(heap, 0, len(heap) - 1)
    return item

