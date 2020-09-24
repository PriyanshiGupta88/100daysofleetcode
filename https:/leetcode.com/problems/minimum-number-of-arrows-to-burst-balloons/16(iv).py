class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        c=(sorted(points, key = lambda x: x[1]))
        t=1
        a=c[0][0]
        b=c[0][1]
        for i in range(1,len(c)):
            if c[i][0]>=b:
                t+=1
                b=c[i][1]
        return t
            
