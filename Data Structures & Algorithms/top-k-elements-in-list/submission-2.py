class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create kvp, map num to freq
        kvp = {}
        for i in nums:
            kvp[i] = 1 + kvp.get(i, 0)

        # create a heap
        h = []
        for i in kvp.keys():
            heapq.heappush(h, (kvp[i], i))
            if len(h) > k:
                heapq.heappop(h)

        # pop the elements and return
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res
        
