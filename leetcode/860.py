class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5 = 0
        change_10 = 0
        change_20 = 0
        for i in range(0,len(bills),1):
            if bills[i] == 5:
                change_5 += 1
            elif bills[i] == 10:
                change_10 += 1
                if change_5 > 0:
                    change_5 -= 1
                else:
                    return False
            elif bills[i] == 20:
                change_20 += 1
                if change_10 > 0 and change_5 > 0:
                    change_10 -= 1
                    change_5 -= 1
                elif change_10 == 0 and change_5 >= 3:
                    change_5 -= 3
                else:
                    return False
        return True