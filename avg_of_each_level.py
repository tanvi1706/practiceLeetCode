class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from queue import Queue
class Solution:
    def averageoflevels(self, root: TreeNode) -> List[float]:
        def avgoflevels(root):
            result = []
            q = Queue()
            q.put(root)
            while not q.empty():
                summ = 0
                count = 0
                temp = Queue()
                while not q.empty():
                    n = q.queue[0]
                    q.get()
                    summ += n.val
                    count += 1
                    if n.left != None:
                        temp.put(n.left)
                    if n.right != None:
                        temp.put(n.right)
                q = temp
                result.append(summ * 1.0 /count)
            return result
        return avgoflevels(root)