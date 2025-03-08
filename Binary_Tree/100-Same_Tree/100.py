# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        eq = p.val == q.val
        print(eq)
        left_node = self.isSameTree(p.left, q.left)
        right_node = self.isSameTree(p.right, q.right)
        return eq and left_node and right_node

if __name__ == '__main__':
    soln = Solution()
    p = [1, 2, 3]
    q = [1, 2, 3]
    print(soln.isSameTree(p, q))
