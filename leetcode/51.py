class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = set()
        pos_diag = set() 
        neg_diag = set() 
        
        res = []
        board = [["."] * n for _ in range(n)]

        def check(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                check(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        check(0)
        return res