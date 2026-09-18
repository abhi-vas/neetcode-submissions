class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones)>1:
            max1 = heapq._heappop_max(stones)
            max2 = heapq._heappop_max(stones)
            if max1 > max2 :
                heapq._heappush_max(stones,max1-max2)
        if len(stones) ==1:
            return stones[0]
        else:
            return 0
