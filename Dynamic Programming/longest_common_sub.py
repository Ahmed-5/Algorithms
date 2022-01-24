import math

memo = {}

def DP(i,j):
    if i < 0:
        return j+1
    if j < 0:
        return i+1
    if (i,j) in memo:
        return memo[(i,j)]

    value = min(1+DP(i-1,j), 1+DP(i,j-1), DP(i-1, j-1) if w1[i]==w2[j] else math.inf)
    memo[(i,j)] = value
    return value



w1 = "hieroglyphology"
w2 = "michaelangelo"

l = len(w1) + len(w2) - DP(len(w1)-1, len(w2)-1)

print(l//2)