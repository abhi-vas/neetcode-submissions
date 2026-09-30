class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        

        if sum(matchsticks)%4 !=0:
            return False
        target =sum(matchsticks)//4

        matchsticks.sort(reverse=True)
        sides=[0]*4

        def back_track(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if sides[j]+matchsticks[i] <=target:
                    sides[j]+=matchsticks[i]
                    if back_track(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False

        return back_track(0)
        