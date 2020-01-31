class DisjointSet:
    def __init__(self, nodeList = []):
        self.parents = nodeList
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        
        if(xp != yp):
            self.parents[xp] = yp

if '__main__' == __name__:
    d = DisjointSet([0, 1, 2, 3, 4, 5, 6])
    print(d.find(1))
    d.union(6, 3)
    d.union(3, 0)
    d.union(4, 0)
    d.union(2, 1)
    d.union(5, 1)
    d.union(0, 1)
    print(d.parents)
    print(d.find(6))
    print(d.parents)
    
