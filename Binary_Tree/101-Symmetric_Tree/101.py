# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def compare_nodes(self, left_node, right_node):
        if left_node == None and right_node == None:
            return True
        if left_node == None or right_node == None:
            return False
        
        nxt_node = left_node.val == right_node.val
        nxt_node1 = self.compare_nodes(left_node.left, right_node.right)
        nxt_node2 = self.compare_nodes(left_node.right, right_node.left)
        return nxt_node and nxt_node1 and nxt_node2

    def isSymmetric(self, root):
        if root == None: 
            return True
        return self.compare_nodes(root.left, root.right)
    

if __name__ == "__main__":
    # Creating a symmetric binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    print("Is the tree symmetric?", solution.isSymmetric(root))  # Expected output: True

    # Creating an asymmetric binary tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    print("Is the tree symmetric?", solution.isSymmetric(root2))  # Expected output: False