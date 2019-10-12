from collections import deque

def bfs(graph, start = None):
    if(graph):
        if(not start):
            start = next(iter(graph))
        explored_nodes = {}
        dq = deque([start])
        while(dq):
            current_node = dq.popleft()
            print(current_node)
            if(current_node in explored_nodes):
                print('Error, node is revisited!')
                break
            explored_nodes[current_node] = 0
            for next_node in graph[current_node]:
                if(next_node not in explored_nodes):
                    dq.append(next_node)
            explored_nodes[current_node] = 1

def dfs_recursive(graph, current_node = None, explored_nodes = {}):
    if(graph):
        if(not current_node):
            current_node = next(iter(graph))
        print(current_node)
        explored_nodes[current_node] = 0
        for next_node in graph[current_node]:
            if(next_node not in explored_nodes):
                explored_nodes = dfs_recursive(graph, next_node, explored_nodes)
        explored_nodes[current_node] = 1
        return explored_nodes
        
        

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [3], 2: [4, 5], 3: [], 4: [], 5: [0] }
    #bfs(graph, 0)
    dfs_recursive(graph, 0)
