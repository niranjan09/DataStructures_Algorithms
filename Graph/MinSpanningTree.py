import sys
sys.path.insert(1, '../')

from DisjointSets import disjointSets

def kruskalsMinSpanningTree(graph):
    edgesList = []
    for node, node_edges in graph.items():
        for node_edge in node_edges:
            edgesList.append((node_edge[1], (node, node_edge[0])))
    #print(edgesList)
    edgesList.sort()
    spanningTree = []
    d = disjointSets.DisjointSet(list(range(len(graph))))
    for edge in edgesList:
        w, u, v = edge[0], edge[1][0], edge[1][1]
        ur = d.find(u)
        vr = d.find(v)
        if(ur != vr):
            d.union(u, v)
            spanningTree.append(edge)
    return spanningTree





if __name__ == '__main__':
    graph = {0: [(1, 1), (2, 2)], 1: [(3, 2)], 2: [(4, 5), (5, 3)], 3: [], 4: [], 5: [(0, 6)] }
    print(kruskalsMinSpanningTree(graph))
    
