class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = []
        for i in range(left,right+1,1):
            l = list(str(i))
            flag = len(l)
            if "0" in str(i):
                continue
            for j in range(0,len(l),1):
                if i % int(l[j]) == 0:
                    flag -= 1
                else:
                    break
                if flag == 0:
                    numbers.append(i)
        return numbers
            