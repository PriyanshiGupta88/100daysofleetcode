class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1
        length = len(primes)
        mul_indices = [0] * length
        multipliers = primes[:]

        for index in range(1, n):
            ugly_nums[index] = min(multipliers)

            for in_index in range(length):
                if ugly_nums[index] == multipliers[in_index]:
                    mul_indices[in_index] += 1
                    multipliers[in_index] = ugly_nums[mul_indices[in_index]] * primes[in_index]

        return ugly_nums[n-1]
