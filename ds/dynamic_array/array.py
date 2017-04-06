class Array:
    def __init__(self, cap=0):
        self.cap = cap
        self.size = 0
        self.rep = [0 for _ in range(self.cap)]

    def __repr__(self):
        return '[{}]'.format(', '.join(map(str, self.rep)))

    def __len__(self):
        return self.size

    def __setitem__(self, i, x):
        if self.size == self.cap:
            self._expand()
        self.rep[i] = x
        self.size += 1

    def __getitem__(self, i):
        return self.rep[i]

    def append(self, x):
        last_index = self.size
        self[last_index] = x

    def _expand(self):
        if not self.cap:
            self.cap = 1
        else:
            self.cap *= 2
        new_rep = Array(self.cap)
        for item in self.rep:
            new_rep.append(item)
        self.rep = new_rep
