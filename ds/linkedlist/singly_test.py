from singly import Link
from functools import partial
from util.link import links_from_list


def test_iter():
	linker = partial(links_from_list, Link)
	ll = linker([2, 4])
	assert set(ll) == {2, 4}


def test_insert():
	ll = Link()
	assert not ll.search(5)

	ll.insert(Link(5))	
	assert ll.search(5).datum == 5


def test_search():
	linker = partial(links_from_list, Link)
	ll = linker([2, 4])

	assert not ll.search(1)
	assert not ll.search(3)
	assert ll.search(2)
	assert ll.search(4)


def test_delete():
	linker = partial(links_from_list, Link)
	ll = linker([2])

	assert ll.search(2)

	ll.delete(Link(2))
	assert not ll.search(2)
