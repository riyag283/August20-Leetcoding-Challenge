class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [0]*num_people
        fill = (int)((2*candies + 0.25)**0.5 - 0.5)
        extra = (int)(candies - (fill*(fill+1)/2))
        x = fill // num_people
        y = num_people * x
        left = fill - y
        for i in range(num_people):
                arr[i] = (int)(x/2 * (2*(i+1) + (x-1)*num_people))
                #print(i,arr[i])
        for i in range(left):
                arr[i] += y + i + 1
                #print(i,arr[i])
        arr[left] += extra
        #print(left, arr[left])
        return arr
