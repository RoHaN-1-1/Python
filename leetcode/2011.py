class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in range(0,len(operations),1):
            if operations[i] == "++X" or operations[i] == "X++":
                x += 1
            elif operations[i] == "--X" or operations[i] == "X--":
                x -= 1
        return x