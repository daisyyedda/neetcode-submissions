class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer
        slow = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
            
        return slow