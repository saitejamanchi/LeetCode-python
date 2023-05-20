"""
Problem: https://leetcode.com/problems/reverse-linked-list/

Solution: We recursively traverse the Linked List while reversing the pointer.

Time Complexity: O(n) as we travel throught the entire length of the list.

Space Complexity: O(1) as we're not creating any additional data structures.	
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLL(self,curr, prev):
        if curr:
            tmp = curr.next
            curr.next = prev
            return self.reverseLL(tmp, curr)
        return prev
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseLL(head, None)
