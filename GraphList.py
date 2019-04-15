from sys import exit


class GraphList(object):
    graph = {}
    nb_sommets = 0

    def __init__(self, nb_sommets):
        self.nb_sommets = nb_sommets

    def ajouter_sommet(self, sommet):
        if sommet not in self.graph.keys():
            self.graph[sommet] = []

    def ajouter_arete(self, s1, s2):
        neighbors1 = self.graph[s1]
        neighbors2 = self.graph[s2]
        neighbors1.append(s2)
        neighbors2.append(s1)

    def supprimer_sommet(self, s):
        self.graph.pop(s)
        for (k, values) in self.graph.items():
            try:
                values.remove(s)
            except Exception:
                pass

    def degre(self, s):
        try:
            list_adjacence = self.graph[s]
            return len(list_adjacence)
        except Exception:
            print("sommet (%d) non existant" % s)
            exit(1)
