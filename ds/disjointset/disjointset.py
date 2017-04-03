import json


class DisjointSet:
    def __init__(self, n):
        self.components = {i: i for i in range(1, n + 1)}

    def __repr__(self):
        return json.dumps(self.components)

    def __str__(self):
        return repr(self)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        return self.components[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        for i, val in self.components.items():
            if val == yset:
                self.components[i] = xset

    def count(self):
        return len(set(self.components.values()))

