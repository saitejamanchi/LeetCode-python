"""
Problem: https://leetcode.com/problems/longest-common-prefix/

Solution: Initially, we consider the first string as common prefix.
We then iteratively check if th common prefix is matching with each string.
If it is not matching we return an empty string.
If it matches partially we make the partially matched string as the new common prefix.

Time Complexity: O(n*m) where n is the total number of string and m is max length of string.

Space Complexity: O(m) as we're creating a common prefix string.

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        common_prefix_len = len(strs[0])
        for s in strs:
            curr_len = 0
            for i in range(min(common_prefix_len, len(s))):
                cur_len = 0
                if common_prefix[i] == s[i]:
                    curr_len += 1
                elif curr_len == 0:
                    return ""
                else:
                    break
            common_prefix = s[:curr_len]
            common_prefix_len = curr_len
        return common_prefix