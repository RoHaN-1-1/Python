class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""
        while n > 0:
            binary += str(n % 2)
            n = n // 2 
        return binary.count("1")