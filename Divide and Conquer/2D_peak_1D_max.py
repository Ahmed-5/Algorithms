def get_peak_col(mat, col_index):
    m = mat[0][col_index]
    row_ind = 0
    for i in range(len(mat)):
        if mat[i][col_index]>m:
            m = mat[i][col_index]
            row_ind = i

    return row_ind

def peak_2D(mat):
    s = 0
    e = len(mat[0])-1
    mid = (e+s)//2
    r = get_peak_col(mat, mid)
    peak = False

    while not peak:
        peak = True
        if mid-1>=0 and mat[r][mid-1]>mat[r][mid]:
            peak = False
            e = mid-1
            mid = (e+s)//2
            r = get_peak_col(mat, mid)
        elif mid+1<len(mat[0]) and mat[r][mid+1]>mat[r][mid]:
            peak = False
            s = mid+1
            mid = (e+s)//2
            r = get_peak_col(mat, mid)
        else:
            return r, mid, mat[r][mid]

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(peak_2D(mat))