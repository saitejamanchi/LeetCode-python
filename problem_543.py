"""
Problem : https://leetcode.com/problems/diameter-of-binary-tree/

Solution : 
For each node in the tree, We recursively calculate the following things:
i) Heights of Left and Right Sub-Tree
ii) Maximum Diameter of the Left and Right Sub-Tree

From the above values, We find the Diameter of the Current Node by adding the heights of left and right Sub-Trees.
We then compare it with the maximum diameter seen so far.
At the end we'll get the maximum daimeter of the give Tree.

Time Complexity : Since we'll be visting each node once, it comes out to be O(n).

Space Complexity : Since we're not using any additional data structures other than the one provided, it would be O(1).


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDiamOfSubTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0, 0
        
        left_diam, left_len = self.getDiamOfSubTree(root.left)
        right_diam, right_len = self.getDiamOfSubTree(root.right)
        
        maxDiam = max(left_diam, right_diam)
        
        if maxDiam < left_len + right_len:
            maxDiam = left_len + right_len
        
        return maxDiam, max(left_len, right_len) + 1     
        
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getDiamOfSubTree(root)[0]