"""
Problem: https://leetcode.com/problems/merge-two-sorted-lists/

Solution: We recursively add the smallest elemnt of the starting nodes of the two list to the newly created list.
By the end we will hav a merge list.

Time Complexity: O(m+n) where m and n are the length of the two linked lists.

Space Complexity: O(1) as we're not creating any additional data structures.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, newListEnd, head1, head2):
        if head1 is None and head2 is None:
            return
        elif head1 is None:
            newListEnd.next = head2
            newListEnd=head2
            return
        elif head2 is None:
            newListEnd.next = head1
            newListEnd=head1
            return
        else:
            if head1.val < head2.val:
                newListEnd.next = head1
                newListEnd = head1
                head1 = head1.next
            else:
                newListEnd.next = head2
                newListEnd = head2
                head2 = head2.next
        return self.mergeList(newListEnd, head1, head2)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        self.mergeList(newHead,list1, list2)
        return newHead.next
        
        