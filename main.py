import GraphMatrice

if __name__ == '__main__':
    G = GraphMatrice.GraphMatrice(4)
    G.ajouter_arete(2, 3)
    G.ajouter_arete(1, 3)
    G.ajouter_arete(1, 2)
    print(G.graph)
    print(G.degre(1))
