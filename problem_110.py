"""
Problem: https://leetcode.com/problems/balanced-binary-tree/submissions/

Solution: We recursively get the height of the left and right sub-trees of each node starting from bottom to top.
We check if the difference between these height is less than or equal 1 for this to be a Balanced Binary Tree.
Otherwise, it is not.

Time Complexity: Since we're visting all the nodes of the tree once the time complexity works out to be O(n).

Space Complexity: O(1) Since we're not creating any additional data structures.


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isTreeBalanced = True
    def isSubTreeBalanced(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.isSubTreeBalanced(root.left)
        right_height = self.isSubTreeBalanced(root.right)
        
        if (abs(left_height - right_height) > 1):
            self.isTreeBalanced = False    
        
        return max(left_height, right_height) + 1
        
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        tmp = self.isSubTreeBalanced(root)
        return self.isTreeBalanced