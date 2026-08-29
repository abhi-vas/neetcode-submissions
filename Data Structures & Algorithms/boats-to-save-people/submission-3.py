class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        i=0
        r=len(people)-1
        res=0


        while i<=r:
            if people[i]==limit:
                res=res+1
                i=i+1
            elif people[r]==limit:
                r=r-1
                res=res+1
            elif people[i]+people[r]==limit:
                i=i+1
                r=r-1
                res=res+1
            elif people[i]+people[r]<limit:
                i=i+1
                r=r-1
                res=res+1
            elif people[i]+people[r]>limit:
                if people[r]<limit:
                    res=res+1
                    r=r-1
                elif people[i]<limit:
                        i=i+1
                        res=res+1
        return res
    
                

                



        
            
                


