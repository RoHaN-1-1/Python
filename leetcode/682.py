class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        current = 0
        for i in range(0,len(operations),1):
            if operations[i] != "C" and operations[i] != "D" and operations[i] != "+":
                record.append(int(operations[i]))
            elif operations[i] == "C":
                record.pop()
            elif operations[i] == "D":
                record.append(int(record[-1]*2))
            elif operations[i] == "+" and len(record) > 1:
                record.append(int(record[-1])+int(record[-2]))
        for i in range(0,len(record),1):
            current += record[i]
        return current