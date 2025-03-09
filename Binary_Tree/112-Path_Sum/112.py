# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        # If it's a leaf node, check if its value matches targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        left_trav = self.hasPathSum(root.left, targetSum - root.val)
        right_trav = self.hasPathSum(root.right, targetSum - root.val)
        if left_trav:
            return True
        if right_trav: 
            return True
        return False 

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    soln = Solution()
    print("Path Sum: ", soln.hasPathSum(root, targetSum=22))