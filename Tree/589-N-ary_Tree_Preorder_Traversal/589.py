class TreeNode():
    def __init__(self, val=0):
        self.val = val
        self.children = []
    
class Solution():
    def preorder(self, root:TreeNode):
        if root == None:
            return 
        node = [root.val]
        for child in root.children:
            node.extend(self.preorder(child))
        return node

if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))
    
    soln = Solution()
    print(soln.preorder(root))