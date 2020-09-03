class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        i = 0
        while i <= len(arr)-3:
            if (arr[i] - arr[i+1]) != (arr[i+1]-arr[i+2]):
                return False
            i+=1
        return True
