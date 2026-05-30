class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a kvp, mapping the nums to their freqs
        kvp = {}
        for i in nums:
            kvp[i] = 1 + kvp.get(i, 0)
        
        # create a max heap based on the value
        heap = []
        for i in kvp.keys():
            heapq.heappush(heap, (kvp[i], i))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        # pop the keys
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
