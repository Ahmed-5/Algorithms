def peak_2D(mat):
    m = len(mat)//2
    n = len(mat[0])//2
    peak = False

    while not peak:
        peak = True
        if m-1>=0 and mat[m-1][n] > mat[m][n]:
            peak = False
            m = m-1
        
        elif m+1<len(mat) and mat[m+1][n]>mat[m][n]:
            peak = False
            m = m+1
        
        elif n-1>=0 and mat[m][n-1]> mat[m][n]:
            peak = False
            n = n-1
        
        elif n+1<len(mat[0]) and mat[m][n+1]> mat[m][n]:
            peak = False
            n = n+1

    return m,n,mat[m][n]


mat = [[1,2,3],[4,5,6],[7,8,9]]
print(peak_2D(mat))