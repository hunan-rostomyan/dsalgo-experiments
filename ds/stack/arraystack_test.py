import pytest

from arraystack import Stack


def test_lifo():
    stack = Stack()

    stack.push(5)
    stack.push(6)
    assert stack.pop() == 6
    assert stack.pop() == 5


def test_push_pop_empty():
    stack = Stack()
    assert stack.empty()

    stack.push(5)
    assert stack.pop() == 5

    assert stack.empty()


def test_pop():
    stack = Stack()
    with pytest.raises(TypeError) as e_info:
        stack.pop()


def test_capacity():
    # Create a stack that can hold a single element only.
    stack = Stack(1)
    assert stack.empty()

    stack.push(5)

    # Attempting to push an additional item should fail.
    with pytest.raises(TypeError) as e_info:
        stack.push(6)
