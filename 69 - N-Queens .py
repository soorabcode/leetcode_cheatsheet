# Day 69 
# N-Queens 
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, d1, d2 = set(), set(), set()
        board = [["."] * n for _ in range(n)]

        def bt(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r-c in d1 or r+c in d2:
                    continue
                board[r][c] = "Q"
                cols.add(c); d1.add(r-c); d2.add(r+c)
                bt(r+1)
                board[r][c] = "."
                cols.remove(c); d1.remove(r-c); d2.remove(r+c)

        bt(0)
        return res