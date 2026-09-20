class Solution:
    def jump(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0

        if nums[0] >= len(nums)-1:
            return 1

        farthestIndex = 0  # 2
        jump = 0
        i = 0
        while (i < len(nums)):

            farthestIndex = max(farthestIndex, i+nums[i])
            if farthestIndex >= len(nums) - 1:
                return jump + 1

            if farthestIndex <= i:
                return -1
            
            maxVal = 0
            maxIndex = -1

            for j in range(i + 1, farthestIndex + 1):
                if j + nums[j] >= maxVal:
                    maxVal = j + nums[j]
                    maxIndex = j

            jump += 1
            i = maxIndex

        return jump