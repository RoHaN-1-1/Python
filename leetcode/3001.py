class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            if a == c:
                if (b<d<f) or (f<d<b):
                    return 2
                else:
                    return 1
            else:
                return 1
        elif b == f:
            if b == d:
                if (a<c<e) or (e<c<a):
                    return 2
                else:
                    return 1
            else:
                return 1
        elif abs(c-e) == abs(d-f):
            if abs(c-a) == abs(d-b):
                if (d<b<f) or (f<b<d):
                    return 2
                else:
                    return 1
            else:
                return 1
        else:
            return 2