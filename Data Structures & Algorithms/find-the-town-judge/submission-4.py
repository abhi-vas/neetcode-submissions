class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming =defaultdict(int)
        outgoing = defaultdict(int)

        for a_i,b_i in trust:
            incoming[b_i]+=1
            outgoing[a_i]+=1

        for i in range(1,n+1):
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i
        return -1