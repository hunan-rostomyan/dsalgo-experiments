class Link():
    def __init__(self, datum=None):
        self.datum = datum
        self.right = None

    def __repr__(self):
        return '({} . {})'.format(self.datum, list(self))

    def __iter__(self):
        cur = self.right
        while cur:
            yield cur.datum
            cur = cur.right

    def search(self, key):
        cur = self.right
        while cur:
            if cur.datum == key:
                return cur
            cur = cur.right

    def insert(self, link):
        link.right = self.right
        self.right = link

    def delete(self, link):
        prev = self       # points to sentinel
        cur = self.right  # points to first or None
        while cur:
            if cur.datum == link.datum:
                prev.right = cur.right
                if cur.right:
                    cur = cur.right.right
                    continue
            prev = cur
            cur = cur.right
