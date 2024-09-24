# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):

       #Base case: empty tree. No sum so return 0
        if root is None:
            return 0
        
        #Compare value of current node if within the [low,high]
        #sum of current node, recursively calls function for left and right substrees
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low , high) + self.rangeSumBST(root.right, low , high)

        #if currenot node > high then out of range. Focus on left side of tree
        if root.val > high:
            return self.rangeSumBST(root.left, low , high)

        #right tree when  current node val < low. The out of range so focus on right side of tree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        