class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        time = {}
        
        for i in itertools.permutations(A):
            if ((i[0]==2 and i[1]<=3) or i[0]<=1) and i[2]<=5:
                x = str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])
                time[int(x)] = x
        
        if time == {}:
            return ""
        
        h = time[max(time)]
        
        return h[:2] + ":" + h[2:]
