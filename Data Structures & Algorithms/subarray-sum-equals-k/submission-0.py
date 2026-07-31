class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currsum = 0
        seen = {0: 1}  # prefix sum 0 has occurred once (before the array starts)
        for num in nums:
            currsum += num
            if (currsum - k) in seen:
                count += seen[currsum - k]
            seen[currsum] = seen.get(currsum, 0) + 1
        return count