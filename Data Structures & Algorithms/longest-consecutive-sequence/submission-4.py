class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # construct the set
        s = set(nums)
        res = 0

        for i in nums:
            if i-1 not in s:
                curr_len = 1
                while i + curr_len in s:
                    curr_len += 1  
                res = max(curr_len, res)
        
        return res
           