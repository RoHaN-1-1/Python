class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        for i in range(1,x//2+3,1):
            if i * i > x:
                return i -1
            elif i * i == x:
                return i  
            else:
                continue
        return 0