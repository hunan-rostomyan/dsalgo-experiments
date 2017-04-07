from functools import partial

from doubly import Link
from util.link import links_from_list


if __name__ == '__main__':
    # A converter from lists to linked lists
    linker = partial(links_from_list, Link)

    ll = linker([3, 2, 1])
    assert list(ll) == [1, 2, 3]

    ll.delete(Link(2))
    assert list(ll) == [1, 3]

    # A linear way to determine the length
    # of the link is to iterate and count.
    assert len(list(ll)) == 2

    # Link is iterable, so all the usual cool
    # things one does with iterables, we can
    # do with it.
    squares = list(map(lambda x: x ** 2, ll))
    assert squares == [1, 9]

    # Finding the extrema is also easy.
    ll = linker([2, 3, 5])
    assert max(ll) == 5
    assert min(ll) == 2

