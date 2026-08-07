class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,value in enumerate(nums):
            comp = target - value
            if comp in dic:
                return ([dic[comp],i])
                break
            dic[value] = i