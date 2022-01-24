memo = {}

def DP(i,j):
    if i < 0:
        return j+1
    if j < 0:
        return i+1
    if (i,j) in memo:
        return memo[(i,j)]

    value = min(1+DP(i-1,j), 1+DP(i,j-1), DP(i-1, j-1) if w1[i]==w2[j] else 1+DP(i-1, j-1))
    memo[(i,j)] = value
    return value



w1 = "abc"
w2 = "ac"

DP(len(w1)-1, len(w2)-1)

for key in memo:
    print(key[0]+1, key[1]+1, memo[key])