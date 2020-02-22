import sys
sys.path.insert(1, '../')

from DisjointSets import disjointSets
import heapq

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


def primsMinSpanningTree(graph, startNode = None):
    if not startNode:
        gitems = list(graph.items())
        startNode = gitems[0][0]
    edgesHeap = []
    spanningTree = []
    visited = [0]*len(graph)
    visited[startNode] = 1
    for ei in graph[startNode]:
        heapq.heappush(edgesHeap, (ei[1], (startNode, ei[0])))
    while(edgesHeap):
        #print(edgesHeap, visited)
        nextEdge = heapq.heappop(edgesHeap)
        if visited[nextEdge[1][1]]:
            continue
        visited[nextEdge[1][1]] = 1
        spanningTree.append(nextEdge)
        for ei in graph[nextEdge[1][1]]:
            if not visited[ei[0]]:
                heapq.heappush(edgesHeap, (ei[1], (nextEdge[1][1], ei[0])))
    return spanningTree        



if __name__ == '__main__':
    graph = {0: [(1, 1), (2, 2), (5, 6)], 1: [(3, 2), (0, 1)], 2: [(4, 5), (5, 3), (0, 2)], 3: [(1, 2)], 4: [(2, 5)], 5: [(0, 6), (2, 3)] }
    #print(kruskalsMinSpanningTree(graph))
    print(primsMinSpanningTree(graph))
