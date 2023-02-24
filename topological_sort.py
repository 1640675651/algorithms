def toposortdfs(al): #al: adjacent list, al[i] stores all vertices that i can reach directly
    vis = [False] * n
    ts = []
            
    for i in range(len(al)): 
        if vis[i] == False:
            toposortdfs_r(i, al, vis, ts)
            
    ts.reverse() 
    return ts

def toposortdfs_r(v, al, vis, ts):
    vis[v] = True
    for i in al[v]:
        if vis[i] == False:
            toposortdfs_r(i)
    ts.append(v) # the only thing added from a standard dfs
    # v is a prerequisite of all i's.
    # appending v to ts after all i's are searched guarantees v appear later than all i's.
    # therefore ts reversed is a topological sort.


from collections import deque
# Kahn's algorithm
def toposortbfs(al):
    ts = []
    # calculate incoming degree
    ind = [0] * len(al)
    for i in al:
        for j in i:
            ind[j] += 1

    q = deque()
    # put all vertices with 0 incoming degree to a queue (maybe priority queue, to satisfy other requirements of the sort)
    for i in range(len(ind)):
        if ind[i] == 0:
            q.append(i)

    while len(q) != 0:
        v = q.popleft()
        ts.append(v)
        # removal of vertex v can cause deduction of incoming degree of other vertices
        for i in al[v]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)

    return ts
    # this time ts does not need to be reversed
