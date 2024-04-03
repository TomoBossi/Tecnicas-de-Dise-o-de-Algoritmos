P = (3, 2, 5, 6)
P = (3, 6, 10)

################################################################################

M = [[None for _ in range(len(P)+1)] for _ in range(len(P))]                    # AstroVoid puede tener a lo sumo N asteroides comprando uno en cada uno de los N días; la matriz es NxN+1

def astrotrade(j, c):
    global P
    global M

    if not M[j][c]:
        if c < 0 or c > j+1:                                                    # j+1 por indexar desde 0 
            M[j][c] =  float('-inf')
        elif not c and not j:                                                   # j==0 por indexar desde 0 
            M[j][c] =  0
        elif c == 1 and not j:                                                  # j==0 por indexar desde 0 
            M[j][c] =  - P[0]
        else:
            M[j][c] = max([
                - P[j] + astrotrade(j-1, c-1),
                + P[j] + astrotrade(j-1, c+1),
                astrotrade(j-1, c)
            ])
    return M[j][c]

print(astrotrade(len(P)-1, 0))                                                  # N-1 por indexar desde 0 
