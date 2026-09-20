class Solution:
    def jump(self, nums: list[int]) -> int:
            if not nums:
                return 0

            if all(element == nums[0] for element in nums):
                return len(nums)-1

            jump = 0
            left = 0
            right = 0
            while right < len(nums)-1:
    # ------------------- This is to find max within sub aaray (left to right) ----------------
                maximum = 0
                for i in range(left, right+1):
                    maximum = max(maximum, i + nums[i])
    # -----------------------------------------------------------------------------------------
                left = i+1
                right = maximum
                jump += 1

            return jump
    # --------------------------------------------------------------------------