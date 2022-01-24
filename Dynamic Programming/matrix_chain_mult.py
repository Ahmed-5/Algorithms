memo = {}

dims = [30, 40, 60, 75, 80, 25, 40, 90, 10]

n = len(dims) - 1

def DP(i, j):
    if i + 1 >= j:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    value = min(dims[i]*dims[k]*dims[j] + DP(i,k) + DP(k,j) for k in range(i+1,j))
    memo[(i,j)] = value
    return value

DP(0, n)

for key in memo:
    print(key, memo[key])
