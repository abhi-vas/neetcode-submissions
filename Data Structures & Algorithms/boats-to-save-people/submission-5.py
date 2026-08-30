class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        i=0
        r=len(people)-1
        res=0


        while i<=r:
            if people[i]+people[r]<=limit:
                i=i+1
            r=r-1
            res=res+1

            
        return res
    
                

                



        
            
                


