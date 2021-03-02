
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int, parent=None) -> TreeNode:
        if root is None:
            return root
        if key > root.val:
            if root.right is not None:
                self.deleteNode(root.right, key, parent=root)
        elif key < root.val:
            if root.left is not None:
                self.deleteNode(root.left, key, parent=root)
        else:
            if root.left is not None and root.right is not None:
                root.val = getMin(root.right)
                self.deleteNode(root.right, root.val, root)
            elif parent is None:
                if root.left is not None:
                    root.val = root.left.val
                    root.right = root.left.right
                    root.left = root.left.left
                elif root.right is not None:
                    root.val = root.right.val
                    root.left = root.right.left
                    root.right = root.right.right
                else:
                    root = None

            elif root == parent.left:
                parent.left = root.left if root.left is not None else root.right
            elif root == parent.right:
                parent.right = root.right if root.right is not None else root.left

        return root


def getMin(node: TreeNode):
    if node.left is None:
        return node.val
    else:
        return getMin(node.left)
