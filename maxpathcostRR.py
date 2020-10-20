def maxPathCost(i,j):
    if (i<0 or i>=r or j<0 or j>=c):
        return -999999

    #fill last row    
    if (i == r-1 or j== c-1):
        return mat[r-1][j - 1]

    return mat[i][j] + max(maxPathCost(i+1,j), maxPathCost(i,j+1))


if  __name__ == "__main__":
    import sys
    t = int(input().strip())

    for ti in range(t):
        mat=[]
        rc = input().strip().split(' ')
        r = int(rc[0])  
        c = int(rc[1])  
        for _ in range(r):
            rowList = list(map(int, input().strip().split(' ')))
            mat.append(rowList)
        print(maxPathCost(0,0))