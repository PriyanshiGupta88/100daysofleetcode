nums=list(map(int,input().split()))
N = len(nums)
if N <= 1: print(N)
lengths = [0] * N #lengths[i] = longest ending in nums[i]
counts = [1] * N #count[i] = number of longest ending in nums[i]

for j, num in enumerate(nums):
    for i in range(j):
        if nums[i] < nums[j]:
            if lengths[i] >= lengths[j]:
                lengths[j] = 1 + lengths[i]
                counts[j] = counts[i]
            elif lengths[i] + 1 == lengths[j]:
                counts[j] += counts[i]
print(lengths)
print(counts)

