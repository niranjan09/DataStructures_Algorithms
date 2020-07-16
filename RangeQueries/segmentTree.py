class DataNode:
    def __init__(self, data = 0):
        self.sum = data
        self.count = 1
        self.min = data
        self.max = data
        self.change = 0
    
    @classmethod
    def combineDataNodes(cls, dataNode1, dataNode2):
        dataNode = DataNode()
        dataNode.sum = dataNode1.sum + dataNode2.sum
        changeSum = dataNode1.change*dataNode1.count + dataNode2.change*dataNode2.count
        dataNode.sum += changeSum
        dataNode.count = dataNode1.count + dataNode2.count
        dataNode.min = min(dataNode1.min + dataNode1.change, dataNode2.min + dataNode2.change)
        dataNode.max = max(dataNode1.max + dataNode1.change, dataNode2.max + dataNode2.change)
        return dataNode
    
    def makeChange(self, change):
        if(self.count>1):
            self.change += change
        else:
            change += self.change
            self.change = 0
            self.sum += change
            self.min += change
            self.max += change
        
    def __str__(self):
        stat1 = 'Sum of elements is:' + str(self.sum + self.count*self.change) +  '\nCount of Elements is:' + str(self.count)
        stat2 = '\nMin value is:' + str(self.min + self.change) + '\nMax value is:' + str(self.max + self.change)
        return stat1 + stat2
        
class SegmentTree:
    def __init__(self, arr = None):
        self.nlen = (len(arr) if arr else 0)
        self.segTree = [None]*(2*self.nlen - 1)
        if arr: self.buildTree(0, arr, 0, self.nlen-1)
    
    def buildTree(self, sti, arr, start, end):
        if(start == end):
            #print(start, sti)
            self.segTree[sti] = DataNode(arr[start])
            return self.segTree[sti]
        mid = start + (end - start)//2
        dataNode1 = self.buildTree(2*sti+1, arr, start, mid)
        dataNode2 = self.buildTree(2*sti+2, arr, mid+1, end)
        self.segTree[sti] = DataNode.combineDataNodes(dataNode1, dataNode2)
        return self.segTree[sti]
    
    def updateArrElement(self, ind = 0, newVal = 0, sti = 0, segStart = 0, segEnd = None, change = 0):
        if not segEnd: segEnd = self.nlen - 1
        if(ind>segEnd or ind<segStart):
            if(change):
                self.segTree[sti].makeChange(change)
            return None
        if(segStart == segEnd):
            self.segTree[sti] = DataNode(newVal + change)
            return self.segTree[sti]
        
        mid = segStart + (segEnd - segStart)//2
        change += self.segTree[sti].change
        leftNode = self.updateArrElement(ind, newVal, 2*sti+1, segStart, mid, change)
        rightNode = self.updateArrElement(ind, newVal, 2*sti+2, mid+1, segEnd, change)
        
        self.segTree[sti].change = 0
        
        if(leftNode and rightNode):
            ansNode = DataNode.combineDataNodes(leftNode, rightNode)
        else:
            ansNode = leftNode or rightNode
        return ansNode
        
    def rangeQuery(self, start, end, sti = 0, segStart = 0, segEnd = None, change = 0):
        if not segEnd: segEnd = self.nlen - 1
        #print(start, end, sti, segStart, segEnd)
        if(start>segEnd or end < segStart):
            if(change):
                self.segTree[sti].makeChange(change)
            return None
        
        if(start<=segStart and end>=segEnd):
            return self.segTree[sti]
        
        mid = segStart + (segEnd - segStart)//2
        leftNode = self.rangeQuery(start, end, 2*sti+1, segStart, mid)
        rightNode = self.rangeQuery(start, end, 2*sti+2, mid+1, segEnd)
        if(leftNode and rightNode):
            ansNode = DataNode.combineDataNodes(leftNode, rightNode)
        else:
            ansNode = leftNode or rightNode
        return ansNode
    
    def updateRangeOfElements(self, rstart = 0, rend = 0, addend = 0, sti = 0, segStart = 0, segEnd = None):
        #print(rstart, rend, addend)
        if not segEnd: segEnd = self.nlen - 1
        if(rstart > segEnd or rend < segStart): return
        if(rstart <= segStart and rend >= segEnd):
            self.segTree[sti].makeChange(addend)
            #print(segStart, segEnd, addend)
        else:
            mid = segStart + (segEnd - segStart)//2
            self.updateRangeOfElements(rstart, rend, addend, 2*sti+1, segStart, mid)
            self.updateRangeOfElements(rstart, rend, addend, 2*sti+2, mid+1, segEnd)

arr = [2, 3, 7, 5, 1, 9, 10, 4]
segmentTree = SegmentTree(arr)
print(segmentTree.rangeQuery(3, 5))
segmentTree.updateRangeOfElements(rstart = 3, rend = 5, addend = -2)
#for si in segmentTree.segTree:
#    print((si.change, si.sum) if si else None)
print(segmentTree.rangeQuery(3, 5))
segmentTree.updateArrElement(3, -2)
print(segmentTree.rangeQuery(3, 5))
