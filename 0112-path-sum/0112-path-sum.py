# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.calcPath(root, targetSum, 0)

    def calcPath(self,root, targetSum, runningSum):
        if root is None:
            return False
        runningSum = runningSum + root.val
        if root.left is None and root.right is None and targetSum == runningSum:
            return True
        return self.calcPath(root.left, targetSum, runningSum) or self.calcPath(root.right, targetSum, runningSum)