# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def traversal(self, node, arr):
        if node == None:
            return
        arr.append(node.val)
        
        self.traversal(node.left, arr)
        self.traversal(node.right, arr)

    def preorderTraversal(self, root: Optional[TreeNode]):
        arr = []
        self.traversal(root, arr)
        return arr

if __name__ == '__main__':
    soln = Solution()
    root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
    print(soln.preorderTraversal(root))