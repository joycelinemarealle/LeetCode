# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        paths = []

        #helper functions for depth first search
        def dfs(node, current_path):
            #if current node is a leaf, then add curr_path to path list
            if not node.left and not node.right:
                paths.append(current_path)
                return
            #if node has left child, go down left subtree
            if node.left:
                dfs(node.left, current_path + "->" + str(node.left.val))

            #if node has right child go right subtree
            if node.right:
                dfs(node.right, current_path + "->" + str(node.right.val))
            
        #if tree empty
        if not root:
            return paths #empty pathlist

        #Start DFS from root node
        dfs(root, str(root.val))

        return paths
       
    """
    :type root: TreeNode
    :rtype: List[str]
    """
        
#start traverse from root
#go to left child if exist or right until leaf reached. Stop traversal and store the path
#start at root , traverse