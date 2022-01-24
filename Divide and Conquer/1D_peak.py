def peak_1D(arr):
    for i in range(len(arr)):
        if i>0 and arr[i-1]>arr[i]:
            continue
        elif i+1 < len(arr) and arr[i+1]>arr[i]:
            continue
        else:
            return i, arr[i]


arr = [0,1,2,3,7,6,4,5,6,7,8,9]
print(peak_1D(arr))