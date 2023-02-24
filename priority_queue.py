import heapq

class minq:
    def __init__(self):
        self.h = []

    def push(self, x):
        heapq.heappush(self.h, x)

    def pop(self):
        return heapq.heappop(self.h)

    def top(self):
        return self.h[0]

    def __len__(self):
        return len(self.h)

class maxq:
    def __init__(self):
        self.h = []

    def push(self, x):
        heapq.heappush(self.h, -x)

    def pop(self):
        return -heapq.heappop(self.h)

    def top(self):
        return -self.h[0]

    def __len__(self):
        return len(self.h)

