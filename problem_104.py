"""
Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

Solution: We recursively find out the maximum of the heights of both left and right sub-trees of each node in the Binary Tree from bottom to top.
At the end we'll be havin the maximum depth of the Binary Tree.

Time Complexity: O(n) as we're visting each node in the tree once.

Space Complexity: Since we're not creating any additional Data Structures it would be O(1).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1