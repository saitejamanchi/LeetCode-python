"""
Problem: https://leetcode.com/problems/linked-list-cycle/

Solution: We take two pointers one slow and one fast. The slow pointer movies ine step at a time while the fast pointer moves two steps at a time.
If there is a cycle in the linked list the slow and fast pointers will meet at some point.

Time Complexity: O(n) as we're iterating over the list and the pointers will meet in couple of loops if there is a cycle.

Space Complexity: O(1) as we're not creating any additional Data Structures.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False