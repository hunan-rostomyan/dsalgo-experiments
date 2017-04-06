from array import Array


def test_append():
    arr = Array()

    arr.append(5)
    assert arr[0] == 5

    arr.append(6)
    assert arr[1] == 6


def test_set_get():
    arr = Array()

    arr[0] = 5
    assert arr[0] == 5
