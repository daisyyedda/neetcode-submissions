class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        currmax = -1
        for i in range(1, n+1):
            currnum = arr[n-i]
            arr[n-i] = currmax
            currmax = max(currnum, currmax)
        return arr