class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        n = []
        s = []
        for i in arr1:
            if i in arr2_set: 
                n.append(i)
            else: 
                s.append(i)
        count = Counter(n)

        sol = []
        for i in arr2:
            sol += [i] * count[i]
        return sol + sorted(s) 