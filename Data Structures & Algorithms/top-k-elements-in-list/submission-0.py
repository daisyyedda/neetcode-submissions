class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a kvp, mapping the nums to their freqs
        kvp = {}
        for i in nums:
            if i in kvp:
                kvp[i] += 1
            else:
                kvp[i] = 1
        
        # create a max heap based on the value
        heap = [(-v, k) for k, v in kvp.items()]
        heapq.heapify(heap)

        res = []
        # pop the first k keys
        for i in range(0, k):
            item = heapq.heappop(heap)
            res.append(item[1])

        return res
