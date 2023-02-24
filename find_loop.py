def findloop_dfs(al, v, vis, instack, stack): # if vertex v can reach some vertex that is on a loop, the loop can be found. In other words, if some vertex was reached from v without finding a loop, it is not on a loop.
    vis[v] = 1
    instack[v] = 1
    stack.append(v)
    for i in al[v]:
        if vis[i] == 0:
            res = findloop_dfs(al, i, vis, instack, stack)
            if res != None:
                return res
        elif instack[i] == 1: # found a loop, if the graph is undirectional, use elif instack[i] == 1 and i != stack[-2]
            for j in range(len(stack)): # find which vertices are on the loop
                if stack[j] == i:
                    res = stack[j:]
                    stack.pop(-1)
                    instack[v] = 0
                    return res
    stack.pop(-1)
    instack[v] = 0

def findloop(al: 'adjacent list'): # suppose each loop is separate. In other words, one vertex can only belong to one loop.
    n = len(al)
    vis = [0] * n
    for i in range(n):
        if vis[i] == 0:
            res = findloop_dfs(al, i, vis, [0]*n, [])
            if res != None:
                return res
