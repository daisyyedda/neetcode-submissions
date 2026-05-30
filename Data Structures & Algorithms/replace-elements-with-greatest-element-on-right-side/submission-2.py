class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        currmax, currint = 0, 0
        # construct prefic array
        # prearr = [5,5,3,2,2,x]
        for i in range(1,n+1):
            currmax = max(currmax, currint)
            currint = arr[n-i]
            arr[n-i] = currmax

        arr[n-1] = -1
        return arr