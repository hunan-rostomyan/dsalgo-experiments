from .. dynamic_array.array import Array


class Stack:
    def __init__(self, cap=float('inf')):
        self.rep = Array()
        self.cap = cap
        self.top = 0

    def __repr__(self):
        return repr(self.rep)

    def push(self, x):
        if self.top >= self.cap:
            raise TypeError('Overflow: at capacity (= {}).'.format(self.cap))
        self.rep[self.top] = x
        self.top += 1

    def pop(self):
        if self.empty():
            raise TypeError('Underflow: nothing to pop.')
        self.top -= 1
        return self.rep[self.top]

    def empty(self):
        return self.top == 0
