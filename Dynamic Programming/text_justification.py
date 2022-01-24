import math

memo = {}

def badness(i, j, page_width):
    total_width = sum(arr[i:j]) + j-i-1
    return pow(page_width-total_width, 3) if total_width<=page_width else math.inf

def DP(i, n, width):
    if i == n:
        return (0, n)
    
    if i in memo:
        return memo[i]
    
    l = [(DP(j, n, width)[0] + badness(i, j, width), j) for j in range(i+1, n+1)]
    # print(l)
    value = min(l)
    # print(value)
    memo[i] = value

    return value

arr = [3, 4, 5, 6, 12, 5, 7, 3, 7, 2, 10, 14]
page = 20
DP(0, len(arr), page)
for i in range(len(arr)):
    print("{}\t{}\t{}".format(i, arr[i], "\t".join(map(str, memo[i]))))