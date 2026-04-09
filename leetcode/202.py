class Solution:
    def isHappy(self, n: int) -> bool:
        current = n
        num = 0
        seen = []

        while True:
            for i in str(current):
                num += int(i) ** 2
            if num == 1:
                return True
            if num in seen:
                return False
            seen.append(num)
            current = num
            num = 0
            