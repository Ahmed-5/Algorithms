memo = []

def recurse(index=0, mini=0, maxi=0):
    if maxi>time:
        return False
    if index == members:
        return True
    return recurse(index+1, min(mini+arr[index], maxi), max(mini+arr[index], maxi)) or recurse(index+1, min(mini, maxi+arr[index]), max(mini, maxi+arr[index]))

def memo_recurse(index=0):
    global memo
    if index == members-1:
        memo = [False]*1_000_001
        memo[0] = True
        memo[arr[index]] = True
        return
    if len(memo) == 0:
        memo_recurse(index+1)
    s = sum(arr[index+1:])
    for i in range(s):
        if memo[i] == True:
            memo[i+arr[index]] = True


t = int(input().rstrip())

for _ in range(t):
    memo = []
    members, time = list(map(int,input().rstrip().split()))
    arr = list(map(int,input().rstrip().split()))
    arr.sort(reverse=True)
    memo_recurse()
    s = sum(arr)
    found = False
    for i in range(s//2, time+1):
        if memo[i]==True:
            found = True
            break
    if found==False:
        print("NO")
    else:
        print("YES")