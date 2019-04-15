import numpy as np


class GraphMatrice(object):
    nb_sommets = 0

    def __init__(self, nb_sommets):
        self.nb_sommets = nb_sommets
        self.graph = np.zeros((nb_sommets, nb_sommets))

    def ajouter_arete(self, s1, s2):
        self.graph[s1][s2] = 1
        self.graph[s2][s1] = 1

    def degre(self, s):
        return sum(self.graph[s])

    def print_graph(self):
        for i in range(self.nb_sommets):
            for j in range(self.nb_sommets):
                print(self.graph[i][j])
            print()
