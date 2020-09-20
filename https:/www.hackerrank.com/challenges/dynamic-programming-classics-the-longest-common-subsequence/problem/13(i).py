def lcs(a, b):
    lengths = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            lengths[i + 1][j + 1] = lengths[i][j] + 1 if x == y else max(lengths[i + 1][j], lengths[i][j + 1])
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:  x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:    y -= 1
        else:
            result = [a[x - 1]] + result
            x -= 1
            y -= 1
    print(" ".join(str(i) for i in result))

n, m = map(int, input().split())
lcs([int(_) for _ in input().split()], [int(_) for _ in input().split()])
