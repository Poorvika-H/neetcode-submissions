class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max  # swap before multiplying
            curr_max = max(nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i])
            max_prod = max(max_prod, curr_max)
        return max_prod