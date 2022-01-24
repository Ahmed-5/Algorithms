def peak_find_1D(arr):
    s = 0
    e = len(arr) - 1

    if e == 0:
        return 0, arr[0]
    elif e == 1:
        if arr[0]>arr[1]:
            return 0, arr[0]
        else:
            return 1, arr[1]

    while s<=e:
        m = (s+e)//2
        print(m, arr[m])
        if m+1 < len(arr) and arr[m+1]>arr[m]:
            s = m+1
        elif m>=0 and arr[m-1]>arr[m]:
            e = m-1
        else:
            return m, arr[m]


arr = [0,1,2,3,7,6,4,5,6,7,8,9]
print(peak_find_1D(arr))