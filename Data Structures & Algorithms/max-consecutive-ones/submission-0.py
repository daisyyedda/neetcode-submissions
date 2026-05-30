class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi, curr = 0, 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                curr = 0
            maxi = max(maxi, curr)
        return maxi