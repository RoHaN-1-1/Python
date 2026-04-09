class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        nums = [number.replace(digit,"",1)]
        for i in range(0,len(number),1):
            if number[i] == digit:
                x = number[:i] + number[i+1:]
                nums.append(x)
        return max(nums)