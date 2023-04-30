"""
Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Solution: We recursively traverse the linked list to find out the position of each node from the end of the list.
When we reach n+1 node in the list we change the next pointer to the next next node in the list i.e., n - 1. Hence reomving the nth element.
One edge case is that the node only has n nodes, we check for this case at the end and return head.next.

Time Complexity: As we're only traversing the list once, it is O(n).

Space Complexity: O(1) as we're not creating any additional data structures.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNthNode(self, head: Optional[ListNode], n: int):
        if not head:
            return 0
        length = self.getNthNode(head.next, n)
        if length + 1 == n + 1:
            head.next = head.next.next
        return length + 1
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = self.getNthNode(head, n)
        if tmp == n:
            return head.next
        return head