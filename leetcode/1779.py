class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        lowest = 10 ** 4
        index = -1
        for i, point in enumerate(points):
            if point[0] == x:
                diff = abs(point[1] - y)
                if diff < lowest:
                    lowest = diff
                    index = i
            elif point[1] == y:
                diff = abs(point[0] - x)
                if diff < lowest:
                    lowest = diff
                    index = i
        return index