from collections import defaultdict

def findArticulationBridges(graph):
    time = 1
    numberNodes = len(graph)
    visited = defaultdict(int)
    disc = defaultdict(int)
    low = defaultdict(int)
    isAB = defaultdict(int)
    def dfs(node, parent = -1):
        visited[node] = 1
        nonlocal time
        low[node] = time
        disc[node] = time
        time+=1
        for nextNode in graph[node]:
            if(nextNode == parent): continue
            if(not visited[nextNode]):
                dfs(nextNode, node)
                low[node] = min(low[node], low[nextNode])
                if(disc[node]<low[nextNode]):
                    isAB[(node, nextNode)] = 1
            else:
                low[node] = min(low[node], disc[nextNode])
        visited[node] = 2
    for node in graph:
        if not visited[node]:
            dfs(node)
    return isAB
            
    
graph = {0:[1, 2], 1:[3, 1], 2:[0], 3:[4, 1], 4:[5, 3], 5:[3, 4]}    
print(findArticulationBridges(graph))
