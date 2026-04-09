class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value = {} 
        numbers = sorted(list(set(arr)))
        
        for i in range(len(numbers)): 
            value[numbers[i]] = i + 1
          
        
        for i in range(len(arr)): 
            arr[i] = value[arr[i]]
        
        return arr 
    