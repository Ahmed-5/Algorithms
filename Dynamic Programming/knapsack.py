import math

memo = {}

ws = [5, 3, 12, 6, 7, 1, 15]
vs = [5, 2, 23, 4, 6, 7, 12]
n = len(ws)

kw = 25

def DP(i, w, n):
    if w < 0:
        return -math.inf
    if i >= n:
        return 0
    if (i,w) in memo:
        return memo[(i,w)]

    value = max(DP(i+1, w, n), DP(i+1, w - ws[i], n) + vs[i])
    memo[(i,w)] = value
    return value

print(DP(0, kw, n))

for key in memo:
    print(key, memo[key])