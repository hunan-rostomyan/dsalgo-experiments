from disjointset_tarjan import DisjointSet


def test_find():
    ds = DisjointSet(5)
    assert ds.find(2) == 2
    assert ds.find(3) == 3


def test_connected():
    ds = DisjointSet(5)
    assert not ds.connected(1, 2)
    ds.union(1, 2)
    assert ds.connected(1, 2)


def test_union():
    ds = DisjointSet(5)
    assert not ds.connected(2, 3)
    ds.union(2, 3)
    assert ds.connected(2, 3)

