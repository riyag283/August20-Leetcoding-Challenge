import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.pre_sum = []
        self.rects = rects
        prev = 0
        for x1, y1, x2, y2 in self.rects:
            count = (x2 - x1 + 1) * (y2 - y1 + 1)
            # self.pre_sum.append(self.pre_sum[-1] + count)
            prev += count
            self.pre_sum.append(prev)
            

    def pick(self) -> List[int]:
        value = random.randrange(self.pre_sum[-1]) + 1
        # bisect_right??
        idx = bisect.bisect_left(self.pre_sum, value)
        value = self.pre_sum[idx] - value
        x1, y1, x2, y2 = self.rects[idx]
        x = x1 + (value % (x2 - x1 + 1))
        y = y1 + (value // (x2 - x1 + 1))
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
