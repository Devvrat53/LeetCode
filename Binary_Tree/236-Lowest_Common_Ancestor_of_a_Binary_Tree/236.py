# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if root == p or root == q:
            return root
        left_trav = self.lowestCommonAncestor(root.left, p, q)
        right_trav = self.lowestCommonAncestor(root.right, p, q)
        if left_trav == None and right_trav == None:
            return None
        elif left_trav == None:
            return right_trav
        elif right_trav == None:
            return left_trav
        else:
            return root

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    soln = Solution()
    print("Lowest Common Ancestor: ", soln.lowestCommonAncestor(root, 5, 1))
