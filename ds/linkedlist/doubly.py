class Link():
    def __init__(self, datum=None):
        self.datum = datum
        self.left = None
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
        if self.right:
            self.right.left = link
        link.left = self
        self.right = link

    def delete(self, link):
        cur = self.right
        while cur:
            if cur.datum == link.datum:
                cur.left.right = cur.right
                if cur.right:
                    cur.right.left = cur.left
                return
            cur = cur.right
