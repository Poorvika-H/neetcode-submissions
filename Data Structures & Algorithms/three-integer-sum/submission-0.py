class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nw=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (nums[i]+nums[j]+nums[k] == 0):
                        if all(sorted([nums[i],nums[j],nums[k]]) != sorted(nw[w]) for w in range(len(nw))):
                            nw.append([nums[i],nums[j],nums[k]])
        return nw
        