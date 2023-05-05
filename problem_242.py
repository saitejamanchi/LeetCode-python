"""
Problem: https://leetcode.com/problems/valid-anagram/

Solution: Create a dictionary to keep track of character and their occurences in the first string.
We then iterate over the second string and subtract the occurences from the dictionary.
After iterating over the second string, we check the dictionary if there are any charcters with other than zero count.
If we find any, it indicates that the two are not anagrams otherwise they are.

Time Complexity: O(n) as we are iterating over the strings and the dict, which has at most n elements.

Space Complexity: O(n) as we're creating a dictionary to store character and their occurences.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = dict()
        for i in s:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        
        for i in t:
            if not i in char_dict:
                return False
            else:
                char_dict[i] -= 1
        
        for key, val in char_dict.items():
            if val != 0:
                return False
        return True