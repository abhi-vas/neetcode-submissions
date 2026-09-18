class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis=[]
        for point in (points):
            dist=(point[0]**2+point[1]**2)**0.5
            dis.append((dist,point))

        dis=sorted(dis,key=lambda x: x[0])

        lst=[]
        m=0
        for dist,point in dis:
            if m>k-1:
                break
            lst.append(point)
            m=m+1
        return lst
        
