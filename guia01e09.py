A = [
    [  -2,  -3,   3],
    [  -5, -10,   1],
    [  10,  30,  -5]
]

m = len(A)
n = len(A[0])

################################################################################

M = [[None for _ in range(n)] for _ in range(m)]

def tv(i, j): # Top-down
    global A
    global m
    global n
    global M

    if not M[i][j]:
        if i == m-1 and j == n-1:
            M[i][j] = max(-A[i][j] + 1, 1)
        elif i == m-1 and j < n-1:
            M[i][j] = max(tv(i, j+1) - A[i][j], 1) 
        elif i < m-1 and j == n-1:
            M[i][j] = max(tv(i+1, j) - A[i][j], 1)
        else:
            M[i][j] = max(min(tv(i+1, j), tv(i, j+1)) - A[i][j], 1)
    return M[i][j]

print(tv(0, 0))

# Todas las operaciones son O(1) y se calculan a lo sumo las N*M
# posiciones de la matriz de memorización, por lo que la complejidad temporal
# es O(N*M). La complejidad espacial es la de las esctructuras 
# (O(N*M)) sumada a la altura máxima del árbol de llamados recursivos 
# (O(max{N,M})), por lo que esta complejidad es también O(N*M).