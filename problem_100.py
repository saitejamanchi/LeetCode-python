"""
Problem: https://leetcode.com/problems/same-tree/

Solution: We recursively go to the nodes in both the trees parallely and see if the both the left sub trees and both the right sub trees are same or not.
We also check if the value of the current node is same or not.
If these checks are passed at all the nodes then at the end we declare both the trees as same, Otherwise not.

Time Complexity: O(n) is the time complexity as we traverse all the nodes in both the trees.

Space Complexity: O(1) as we are not creating any additional data structures.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not(p or q):
            return True
        
        if not(p and q):
            return False
        
        leftSubTreeCheck = self.isSameTree(p.left, q.left)
        rightSubTreeCheck = self.isSameTree(p.right, q.right)
        
        if not (leftSubTreeCheck and rightSubTreeCheck and p.val == q.val):
            return False
        
        return True	