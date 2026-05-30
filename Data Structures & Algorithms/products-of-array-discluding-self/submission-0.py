class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix array, left and right
        l = [0] * len(nums)
        r = [0] * len(nums)
        l[0] = nums[0]
        r[0] = nums[len(nums)-1]
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i]
            r[i] = r[i-1] * nums[len(nums)-i-1]
        
        res = [0] * len(nums)
        res[0] = r[len(nums)-2]
        res[len(nums)-1] = l[len(nums)-2]
        for i in range(1, len(nums)-1):
            res[i] = l[i-1] * r[len(nums)-2-i]

        return res