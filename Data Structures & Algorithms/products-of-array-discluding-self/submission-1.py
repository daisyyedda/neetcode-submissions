class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix array, left and right
        n = len(nums)
        l = [0] * n
        r = [0] * n
        res = [0] * n
        l[0] = r[n-1] = 1
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        for i in range(n):
            res[i] = l[i] * r[i]
        return res