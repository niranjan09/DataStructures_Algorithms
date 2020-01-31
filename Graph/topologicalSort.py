from collections import deque

def topologicalByBFS(graph, start = None):
    inCount = {}
    exploredNodes = {}
    dq = deque()
    for node in graph:
        inCount[node] = 0
        exploredNodes[node] = 0
    if(not start):
        for nodeList in graph.values():
            for node in nodeList:
                if node in inCount:
                    inCount[node] += 1
    for nodeitem in inCount.items():
        if(nodeitem[1] == 0):
            dq.append(nodeitem[0])
            #exploredNodes[nodeitem[0]] = 0
    topologicalOrder = []
    while(dq):
        current_node = dq.popleft()
        if(exploredNodes[current_node] == 0):
            if inCount[current_node] == 0:
                topologicalOrder.append(current_node)
                exploredNodes[current_node] = 1
                for neighbornode in graph[current_node]:
                    inCount[neighbornode] -= 1
                    if inCount[neighbornode] == 0:
                        dq.append(neighbornode)
        elif exploredNodes[current_node] == 1:
            continue
    if(len(topologicalOrder) == len(graph)):
        return topologicalOrder
    else:
        return []
            

#graph with cycle
graph = {0: [1, 2], 1: [3], 2: [4, 5], 3: [], 4: [], 5: [0], 6:[0] }
#graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [5, 6], 5: [6], 6: []}
print(topologicalByBFS(graph))
