class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kvp = {}
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in kvp:
                return [kvp[comp], i]
            kvp[nums[i]] = i
        return [0, 0]