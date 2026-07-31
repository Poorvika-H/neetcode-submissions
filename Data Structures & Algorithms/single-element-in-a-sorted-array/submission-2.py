class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res=0
        for i in range(0,len(nums)-2,2):
            if(nums[i]!=nums[i+1]):
                res=nums[i]
                break
        return res
        