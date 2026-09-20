class Solution:



    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # skip zero counts so they never get placed
        maxheap = [[cnt, ch] for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')) if cnt > 0]
        heapq.heapify_max(maxheap)
        q = deque()
        res = []
        time = 0

        while maxheap or q:
            time += 1
            if not maxheap:
                break                              # only blocked chars remain, nothing valid to place

            freq, ch = heapq.heappop_max(maxheap)
            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                q.append([freq, ch, time + 1])     # blocked: wait one step
            else:
                res.append(ch)
                freq -= 1
                if freq > 0:
                    heapq.heappush_max(maxheap, [freq, ch])   # back immediately, no cooldown

            if q and q[0][-1] <= time:
                freq, ch, _ = q.popleft()
                heapq.heappush_max(maxheap, [freq, ch])

        return ''.join(res)