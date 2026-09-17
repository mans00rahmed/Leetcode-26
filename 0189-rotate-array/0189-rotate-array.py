class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums) if len(nums) > 0 else 0

        # Slice from the start to the pivot, and from the pivot to the end
        first_part = nums[:len(nums)-k]
        second_part = nums[len(nums)-k:]  # Fixed: changed from nums[k:]

        nums[:] = second_part + first_part
        