class Solution:
    def hIndex(self, citations: List[int]) -> int:
        num = 0
        n = len(citations)
        citations.sort(reverse=True)
        for i in range(n):
            num = max(num, min(i+1, citations[i]))
        return num
