class unionfind:
    def __init__(self, n):
        self.parent = list(i for i in range(n))
        self.weight = [1]*n
        
    def find(self, n): # find the root of index n
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n]) # path compression
        return self.parent[n]

    def union(self, a, b):
        self.weight[self.find(a)] += self.weight[self.find(b)] # note 1: update weight before updating parent
        self.parent[self.find(b)] = self.find(a) # let the root of a be the root of b
