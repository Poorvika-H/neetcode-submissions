class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        eg = nums1[:m]
        eg.extend(nums2)
        eg.sort()
        nums1[:] = eg
        