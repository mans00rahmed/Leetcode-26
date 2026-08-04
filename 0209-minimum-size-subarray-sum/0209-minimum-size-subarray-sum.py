class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        result = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]          # O(1) — add incoming element

            while window_sum >= target:
                result = min(result, right - left + 1)
                window_sum -= nums[left]       # O(1) — remove outgoing element
                left += 1

        return result if result != float('inf') else 0
