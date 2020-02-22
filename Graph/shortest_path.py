import heapq
import bisect

#def minHeapify()

def dijkstra(graph, start, target):
    heap = []
    visited = [0]*len(graph)
    weights = {}
    for node in graph:
        weights[node] = 10**10
    weights[start] = 0
    heapq.heappush(heap, (0, start))
    while(not visited[target]):
        nextnode = heapq.heappop(heap)
        visited[nextnode[1]] = 1
        for ni in graph[nextnode[1]]:
            if(weights[ni[0]] > weights[nextnode[1]] + ni[1]):
                weights[ni[0]] = weights[nextnode[1]] + ni[1]
                heapq.heappush(heap, (weights[nextnode[1]] + ni[1], ni[0]))
    return weights[target]

    
def floyd_warshall(graph):
    # initializing 0-matrix to store all pairwise distances
    d, glen = [[float('inf')]*len(graph) for i in range(len(graph))], len(graph)
    index_node_arr, node_index_dict = [0]*glen, {}
    # un-comment following code, and modify the remaining function, 
    # if nodes are not numbered in sequential fashion.
    #for ni, node in enumerate(graph):
    #    index_node_arr[ni] = node
    #    node_index_dict[node] = ni
    
    # for k = -1(or 0 if nodes start from 1), we store weights of edges in matrix
    for ni in range(glen):
        for ei, di in graph[ni]:
            d[ni][ei] = di
            d[ei][ni] = di
        d[ni][ni] = 0
    # for k from 0 to glen-1, we take k as intermediate node and calculate distance,
    # we check whether that distance is better than the previous answer
    for k in range(glen):
        for i in range(glen):
            for j in range(glen):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
    

    

if __name__ == '__main__':
    graph = {0: [(1, 1), (2, 2), (5, 6)], 1: [(3, 2), (0, 1)], 2: [(4, 5), (5, 3), (0, 2)], 3: [(1, 2)], 4: [(2, 5)], 5: [(0, 6), (2, 3)] }
    #print(dijkstra(graph, 0, 5))
    print(floyd_warshall(graph))
