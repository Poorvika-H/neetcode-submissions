class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        n= len(nums)
        for ele in set(nums):
            if nums.count(ele)>(n//3):
                res.append(ele)
        return res
        