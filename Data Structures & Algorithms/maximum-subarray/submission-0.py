class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = -999999999999999999999
        max_sum = -999999999999999999999
        for i in range(len(nums)):
            currsum = max(nums[i],nums[i]+currsum)
            if currsum>max_sum:
                max_sum = currsum
        return max_sum
        