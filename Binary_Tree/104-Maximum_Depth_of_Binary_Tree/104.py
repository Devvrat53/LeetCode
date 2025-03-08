from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # using DFS recursion
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # BFS Iterative approach using queue
    def maxDepthBFSIterative(self, root):
        if root is None:
            return 0
        level = 0
        que = deque([root])
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
        return level
    
    # DFS Preorder Iterative approach using stack
    def maxDepthDFSPreorderIterative(self, root):
        if root is None:
            return 0
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    soln = Solution()

    # print("Maximum Depth of tree", soln.maxDepth(root))
    # print("Maximum Depth of tree", soln.maxDepthBFSIterative(root))
    print("Maximum Depth of tree", soln.maxDepthDFSPreorderIterative(root))