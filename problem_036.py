"""
Problem Statement: https://leetcode.com/problems/valid-sudoku/

Solution: We first check row by row if there is any duplicate element.
Then we check each column. At the end we check each 3*3 square for duplicate elements.
If we don't find any duplicates then it is a Valid sudoku, Otherwise not.

Time Complexity: O(1) as there is no variamce in the input.

Space Complexity: O(1) as we're creating a set that is at most of size 9.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        curr_ele = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in curr_ele:
                    return False
                if board[i][j] != ".":
                    curr_ele.add(board[i][j])
            curr_ele = set()
        
        curr_ele = set()
        
        for i in range(9):
            for j in range(9):
                if board[j][i] in curr_ele:
                    return False
                if board[j][i] != ".":
                    curr_ele.add(board[j][i])
            curr_ele = set()
            
        curr_ele = set()
        
        sub_matrix_start_inds = [0, 3, 6]
        
        for h_start in sub_matrix_start_inds:
            for v_start in sub_matrix_start_inds:
                for i in range(h_start, h_start + 3):
                    for j in range(v_start, v_start + 3):
                        if board[i][j] in curr_ele:
                            return False
                        if board[i][j] != ".":
                            curr_ele.add(board[i][j])
                curr_ele=set()
        return True