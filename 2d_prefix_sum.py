def prefixsum(matrix):
    row = len(matrix)
    col = len(matrix[0])
    ps = []
    for i in range(row):
        ps.append([0]*col)

    ps[0][0] = matrix[0][0]
    for i in range(1, row, 1):
        ps[i][0] = ps[i-1][0] + matrix[i][0]
    for i in range(1, col, 1):
        ps[0][i] = ps[0][i-1] + matrix[0][i]
    
    for i in range(1, row, 1):
        for j in range(1, col, 1):
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i][j]

    return ps

def getsum(ps, r1, c1, r2, c2):
    if r1 == 0 and c1 != 0:
        return ps[r2][c2] - ps[r2][c1-1]
    if c1 == 0 and r1 != 0:
        return ps[r2][c2] - ps[r1-1][c2]
    if r1 == 0 and c1 == 0:
        return ps[r2][c2]
    return ps[r2][c2] - ps[r2][c1-1] - ps[r1-1][c2] + ps[r1-1][c1-1]
