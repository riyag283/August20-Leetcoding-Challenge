class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 1 :
            return [1]
        elif rowIndex == 1:
            return [1,1]
        pascal = [1]
        for i in range(1,rowIndex+1):
            pascal = [1] + pascal
            for j in range(1,i):
                pascal[j] += pascal[j+1]
        return pascal
