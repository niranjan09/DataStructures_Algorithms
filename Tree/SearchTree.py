class TreeNode:
    def __init__(self, val = 0, left = None, right = None, offset = 0, cumsum = 0):
        self.leftNode = left
        self.rightNode =  right
        self.value = val
        self.offset = offset
        self.cumulativeSum = cumsum
    
def searchNode(node, val):
    if(node.value == val):
        return node
    elif(node.value > val):
        if(node.leftNode):
            return searchNode(node.leftNode, val)
        else:
            return False
    else:
        if(node.rightNode):
            return searchNode(node.rightNode, val)
        else:
            return False

a1 = TreeNode(5)
a2 = TreeNode(5)
a3 = TreeNode(5)
a4 = TreeNode(5)
a5 = TreeNode(5)
a6 = TreeNode(5)
a7 = TreeNode(5)
a8 = TreeNode(5)
a9 = TreeNode(5)

