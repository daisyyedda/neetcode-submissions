class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        # find the potential starting points
        seen = set()
        arr = []
        for i in nums:
            seen.add(i)
            if i-1 not in seen:
                arr.append(i)

        # construct the set
        s = set()
        for i in nums:
            s.add(i)

        res = 0
        i = 0
        while i < len(arr):
            start_num = arr[i]
            curr_len = 1
            while start_num + 1 in s:
                curr_len += 1
                start_num += 1   
            res = max(curr_len, res)
            i += 1   
        
        return res



            