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

# Note: call stack method for cycles might give TLE error, when cycles are sub-cycles of 
# large cycles and we revisit each cyle backwards; in those cases use rank method, or dont
# traverse the cycle through stack, just make proper use of recursion.
def dfs_recursive(graph, current_node = None, explored_nodes = {}, call_stack = []):
    if(graph):
        if(not current_node):
            current_node = next(iter(graph))
        print(current_node)
        explored_nodes[current_node] = 0
        call_stack.append(current_node)
        for next_node in graph[current_node]:
            if(next_node not in explored_nodes):
                explored_nodes = dfs_recursive(graph, next_node, explored_nodes, call_stack)
            elif(explored_nodes[next_node] == 0):
                print("Cycle detected", call_stack)
        call_stack.pop()
        explored_nodes[current_node] = 1
        return explored_nodes

def dfs_stack(graph, start_node = None):
    if(graph):
        if(not start_node):
            start_node = next(iter(graph))
        stack = [start_node]
        explored_nodes = {start_node:0}
        while(stack):
            print(stack, explored_nodes)
            current_node = stack[-1]
            if(explored_nodes[current_node] != 0):
                explored_nodes[current_node] = 2
                stack.pop()
                continue
            else:
                explored_nodes[current_node] = 1
                print(current_node)
                for next_node in graph[current_node]:
                    if(next_node not in explored_nodes):
                        stack.append(next_node)
                        explored_nodes[next_node] = 0
                    elif explored_nodes[next_node] == 1:
                        print("Cycle detected")
                
            
                

if __name__ == '__main__':
    #graph = {0: [1, 2], 1: [3], 2: [4, 5], 3: [], 4: [], 5: [0] }
    graph = {0: [1], 1:[2], 2:[3], 3:[4], 4:[5], 5:[2]}
    #bfs(graph, 0)
    dfs_stack(graph, 0)
    #dfs_recursive(graph)
