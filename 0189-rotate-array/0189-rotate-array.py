class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums) if len(nums) > 0 else 0

        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        