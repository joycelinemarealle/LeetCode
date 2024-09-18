
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Inorder Traverse. DFS (depth-first-search)
#keep track of total and when at node check with target


class Solution:
  def hasPathSum(self, root, targetSum):
    #currentSum need to be passed and outer paremeter does not have
        def dfs (node, curSum):
            
            #Base Case Empty Tree
            if not node:
                return False #since no root to leaf path
            
            #Updating sum as going through the node
            curSum += node.val

            #Check if leaf node(then no children)
            if not node.left and not node.right:
                return curSum == targetSum
                
                #Recursively check the left and right subtree
            return dfs(node.left, curSum) or dfs(node.right,curSum)

       
        return dfs(root,0)
