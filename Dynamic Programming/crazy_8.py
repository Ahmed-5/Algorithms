from random import seed, randint

seed(0)

memo = {}

crazies = [[randint(1,13), randint(1,4)] for i in range(8)]

def match(i,j, n):
    if i>= n or j>=n:
        return False
    c1 = crazies[i]
    c2 = crazies[j]
    if c1[0] == 8 or c2[0] == 8 or c1[0] == c2[0] or c1[1] == c2[1]:
        return True
    else :
        return False
    

def DP(i, n):
    if i>=n:
        return 0
    if i in memo:
        return memo[i]

    value = max(1 + DP(j, n) if match(i,j, n) else 1 for j in range(i+1, n+1))
    memo[i] = value
    return value

print(DP(0, len(crazies)))

# for c in crazies:
#     print(*c)

# print()

# for key in memo:
#     print(key, memo[key])