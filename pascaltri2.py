class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        for i in range(rowIndex):
            pascal.append(pascal[i]*(rowIndex-i)//(i+1))
        return pascal
