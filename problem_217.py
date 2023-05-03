"""
Problem: https://leetcode.com/problems/contains-duplicate/

Solution: Create a hashset to keep track of the elements seen so far.
We iterate over the list to see if the present element is already seen in the past by looking up the hashset.
If so, We return true. If we don;t find any duplicate even after iterating the whole list we return false.

Time Complexity: O(n) since we are iterating over the whole list in the worst case scenario.
Since Looking up the hashset is a constant time operation, it doesn't affect time complexity.

Space Complexity: O(n) since in the worst case we'll be storing all the elements of the list in the hashset.

"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in nums:
            if not i in num_set:
                num_set.add(i)
            else:
                return True
        return False