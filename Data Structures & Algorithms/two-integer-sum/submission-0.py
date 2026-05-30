class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, val in enumerate(nums):
            if target-val in mp:
                return [mp[target-val], idx]
            mp[val] = idx
        return [mp[target-val], idx]