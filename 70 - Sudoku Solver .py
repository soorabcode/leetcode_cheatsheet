# Day 70 
# Sudoku Solver 
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(r, c, ch):
            # check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            
            for i in range(9):
                if board[i][c] == ch:
                    return False
            
            start_r, start_c = (r // 3) * 3, (c // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_r + i][start_c + j] == ch:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in map(str, range(1, 10)):
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = '.' 
                        return False
            return True

        backtrack()