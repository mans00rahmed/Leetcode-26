class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums = [2,16,14,15]
        target = 20
        left = 0
        window_state = []
        result = float('inf')
        
        if sum(nums) < target:
            print(0)
        else:
            for right in range(len(nums)):
                window_state.append(nums[right])
        
                while sum(window_state) >= target:
                    result = min(result, len(window_state))   # record length while valid
                    window_state.pop(0)                        # remove from the LEFT, not min
                    left += 1
        
            print(result)
