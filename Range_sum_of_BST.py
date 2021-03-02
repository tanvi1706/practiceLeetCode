# 938 leetcode:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32

# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
#Output: 23
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int, summ=0) -> int:
        summ = 0
        stacl = [root]
        while stacl:
            node = stacl.pop()
            if node:
                if node.val >= low and node.val <= high:
                    summ = summ + node.val
                if low < node.val:
                    stacl.append(node.left)
                if high > node.val:
                    stacl.append(node.right)
        return summ
