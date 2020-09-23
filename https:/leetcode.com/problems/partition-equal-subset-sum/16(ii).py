class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2 != 0: return False
        subSum = numSum // 2
        dp = [True] + [False] * subSum
        for num in nums:
            for i in range(subSum, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[subSum]
