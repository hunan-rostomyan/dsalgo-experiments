class DisjointSet:
    def __init__(self, capacity=0):
        self.forest = [i for i in range(capacity)]

    def __repr__(self):
        return '{}'.format(list(self.forest))

    def find(self, x):
        cur = self.forest[x]
        while cur != self.forest[cur]:
            cur = self.forest[cur]
        return cur

    def union(self, x, y):
        self.forest[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)
