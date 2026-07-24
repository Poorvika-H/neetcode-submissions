class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while(left<=right):
            mid = (left+right)//2
            sum = 0
            for num in piles:
                sum += (num+mid-1)//mid
            
            if(sum<=h):
                right = mid-1
            else:
                left = mid+1

        return left
