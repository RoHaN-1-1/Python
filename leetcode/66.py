class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = digits
        list2 = []
        intlist1 = 0
        for i in range(0,len(list1),1):
            intlist1 = intlist1 * 10 + list1[i]
        intlist1 += 1
        strlist1 = str(intlist1)
        for i in strlist1:
            list2.append(int(i))
        return list2