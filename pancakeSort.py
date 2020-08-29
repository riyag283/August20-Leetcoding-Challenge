class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if len(A)==1:
            return []
        max_pos = A.index(max(A))
        A[0:max_pos+1] = A[0:max_pos+1][::-1]
        A = A[::-1]
        return [max_pos+1, len(A)] + self.pancakeSort(A[:-1])
