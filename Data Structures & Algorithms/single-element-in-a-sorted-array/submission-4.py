class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res=nums[len(nums)-1]
        for i in range(0,len(nums)-2,2):
            if(nums[i]!=nums[i+1]):
                res=nums[i]
                break
        return res
        