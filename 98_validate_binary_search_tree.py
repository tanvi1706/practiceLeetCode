class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validd(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >=high:
                return False
            lefttree = validd(root.left, low, root.val)
            righttree = validd(root.right, root.val, high)
            return lefttree and righttree
        return validd(root, float("-inf"), float("inf"))
