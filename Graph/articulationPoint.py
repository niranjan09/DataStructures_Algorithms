from collections import defaultdict

def findArticulationPoints(graph):
    visited = defaultdict(int)
    disc = defaultdict(int)
    low = defaultdict(int)
    isAP = defaultdict(int)
    time = 1
    def dfs(node, parent = -1):
        nonlocal time
        visited[node] = 1
        low[node] = time
        disc[node] = time
        time+=1
        cc = 0
        for nn in graph[node]:
            if nn==parent: continue
            if(visited[nn]):
                low[node] = min(low[node], disc[nn])
            if(not visited[nn]):
                dfs(nn, node)
                low[node] = min(low[node], low[nn])
                if(low[nn]>=disc[node] and parent != -1):
                    isAP[node] = 1
                cc += 1
        if(parent==-1 and cc>1):
            isAP[node] = 1
        visited[node] = 2
    for node in graph:
        if not visited[node]:
            dfs(node)
    return isAP

#graph = {0: [1, 2], 1: [3], 2: [4, 5], 3: [], 4: [], 5: [0] }
graph = {0: [1], 1:[2, 0], 2:[3, 1, 5], 3:[4, 2], 4:[5, 3], 5:[2, 4], 6:[7], 7:[6, 8], 8:[9, 7], 9:[8]}
print(findArticulationPoints(graph))
