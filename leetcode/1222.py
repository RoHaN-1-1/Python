class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [ [ 0, 1 ], [ 1, 1 ], [ 1, 0 ], [ 1, -1 ], [ 0, -1 ], [ -1, -1 ], [ -1, 0 ], [ -1, 1 ] ]
        sol = []
        row,col = king 
        for i in directions:
            row, col = king
            drow, dcol = i
            while True:
                row += drow
                col += dcol
                if row < 0 or row > 7 or col < 0 or col > 7:
                    break
                cords = [ row, col ]
                if cords in queens:
                    sol.append( cords )
                    break
        return sol