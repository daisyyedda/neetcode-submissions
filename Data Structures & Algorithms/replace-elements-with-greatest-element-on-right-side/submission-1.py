class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prearr = [0] * n
        currmax, currint = 0, 0
        # construct prefic array
        # prearr = [5,5,3,2,2,x]
        for i in range(1,n+1):
            currmax = max(currmax, currint)
            currint = arr[n-i]
            prearr[n-i] = currmax

        # update the original arr
        for i in range(n):
            arr[i] = prearr[i]

        arr[n-1] = -1
        return arr