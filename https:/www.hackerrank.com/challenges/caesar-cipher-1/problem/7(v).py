N = int(input())
a = list(input())
K = int(input())

for i in range(0, N):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if a[i] in list(lower):
        a[i] = lower[(list(lower).index(a[i]) + K) % 26]
    elif a[i] in list(upper):
        a[i] = upper[(list(upper).index(a[i]) + K) % 26]

print(''.join(a))
