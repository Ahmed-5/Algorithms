def get_max_col(mat, col_index):
    s = 0
    e = len(mat) - 1
    
    if e == 0:
        return 0, mat[0][col_index]
    elif e == 1:
        if mat[0][col_index]>mat[1][col_index]:
            return 0, mat[0][col_index]
        else:
            return 1, mat[1][col_index]

    while s<=e:
        m = (s+e)//2
        if m+1 < len(mat) and mat[m+1][col_index]>mat[m][col_index]:
            s = m+1
        elif m>=0 and mat[m-1][col_index]>mat[m][col_index]:
            e = m-1
        else:
            return m, mat[m][col_index]

def peak_2D(mat):
    s = 0
    e = len(mat[0])-1
    mid = (e+s)//2
    r,_ = get_max_col(mat, mid)
    peak = False

    while not peak:
        peak = True
        if mid-1>=0 and mat[r][mid-1]>mat[r][mid]:
            peak = False
            e = mid-1
            mid = (e+s)//2
            r,_ = get_max_col(mat, mid)
        elif mid+1<len(mat[0]) and mat[r][mid+1]>mat[r][mid]:
            peak = False
            s = mid+1
            mid = (e+s)//2
            r,_ = get_max_col(mat, mid)
        else:
            return r, mid, mat[r][mid]

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(peak_2D(mat))