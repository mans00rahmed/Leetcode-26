# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.calcDept(root)
    
    def calcDept(self,root):
        if root is None:
            return 0
        left = self.calcDept(root.left)
        right = self.calcDept(root.right)
        
        return 1+max(left,right)
        