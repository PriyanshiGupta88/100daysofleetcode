class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # time 0: profit 0
        dp = [[0,0]]
        
        #find the max profit before time 
        def find(time):
            i = bisect_left(dp,[time+1])-1
            return dp[i][1]

            
        for s, e, p in jobs:
            dp.append([e,max(find(e),find(s)+p)])
        #print(dp)
        return dp[-1][1]
