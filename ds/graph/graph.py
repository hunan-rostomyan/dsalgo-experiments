import json
import os

from util import from_csv


DATA_INDICES = {
    'label': (0, str),
    'weight': (1, int),
}

SAVE_DIR = 'data/graph/saved/'


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = list(nodes)
        self.labeled_edges = edges
        self.edges = []
        self.data = {}  # e.g. weights

        # Adjacency matrix
        n = len(self.nodes)
        self.matrix = [[0] * n for _ in range(n)]

        # Populate matrix, extract edges and data
        for fro, to, *data in edges:
            edge = (fro, to)
            fro_i, to_i = self.nodes.index(fro), self.nodes.index(to)
            self.edges.append(edge)
            self.matrix[fro_i][to_i] = 1
            if data:
                self.data[edge] = data

        # Adjacency list
        self.adjlist = {node: [to for fro, to in self.edges if fro == node]
                        for node in self.nodes}

    def __repr__(self):
        return json.dumps(self.edges)

    def __str__(self):
        return 'Graph on {}'.format(self.nodes)

    @staticmethod
    def load(filename, root=SAVE_DIR):
        with open(root + filename) as f:
            return Graph(**json.load(f))

    def save(self, filename, root=SAVE_DIR):
        os.makedirs(os.path.dirname(root + filename), exist_ok=True)
        with open(root + filename, 'w') as f:
            json.dump(dict(nodes=self.nodes, edges=self.labeled_edges), f)

    # Weighted Graph specific
    def weight(self, edge):
        i, t = DATA_INDICES['weight']
        return t(self.data[edge][i])

    def weighted_edges(self):
        return [(fro, to, self.weight((fro, to))) for fro, to in self.edges]

