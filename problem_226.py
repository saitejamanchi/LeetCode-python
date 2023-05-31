"""
Problem: https://leetcode.com/problems/invert-binary-tree/

Solution: We recursively swap the left and right SubTrees of each node in the tree.
Time Complexity: O(2^n) where n is the total levels of the tree.

Space Complexity: O(1) as we're not creating any additional DataStructures.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root