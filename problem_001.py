"""
Problem : https://leetcode.com/problems/two-sum/
Solution : We use a dictionary to keep track of the numbers(compliment of numbers), index we've seen so far.
While iterating, we check if the number is already present in the dictionary.
If so, we found the pair and return the indices. Otherwise we add the complimentof number to the dictionary.

Time Complexity : In the worst case We'll loop through all the elements in the list.
				  Since fetching an element from a dictionary is a constant time operation, the overall time complexity is O(n).
				  
Space Complexity : In the worst case we'll find the match at the last element.
				   By that point we'll be storing n - 1 values in the dictionary.Hence Space Complexity comes out to O(n).	
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_tracker = dict()
        for i, j in enumerate(nums):
            if j in num_tracker:
                return num_tracker[j], i
            num_tracker[target - j] = i