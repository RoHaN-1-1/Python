class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1, s2, s3 = str(num1), str(num2), str(num3)

        for i in range(4-len(s1)):
            s1 = "0" + s1
        for i in range(4-len(s2)):
            s2 = "0" + s2
        for i in range(4-len(s3)):
            s3 = "0" + s3
        
        key = ""

        for i in range(4):
            key += str(min(int(s1[i]), int(s2[i]), int(s3[i])))
        
        return int(key)