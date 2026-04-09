class Solution:
    def distMoney(self, money: int, children: int) -> int:
        remaining_money = money - children
        people = remaining_money // 7
        remaining = remaining_money % 7
        if money == children:
            return 0 
        elif people == children and remaining == 0:
            return people
        elif people == children - 1 and remaining == 3:
            return people - 1
        elif people == children and remaining == 3:
            return people - 1 
        elif people > children:
            return children - 1

        elif money < children:
            return -1
        elif people == children and remaining != 0 and remaining != 3:
            return people - 1
        
        return people