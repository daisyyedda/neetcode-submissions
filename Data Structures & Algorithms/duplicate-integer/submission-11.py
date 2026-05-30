class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) < 2:
            return False
        
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]: return True
        return False
