class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for k in nums:
            if k in seen:
                return True
            if k not in seen:
                seen[k] =1
        return False
        