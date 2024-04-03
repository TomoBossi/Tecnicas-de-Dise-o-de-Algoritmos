N = 4
K = 3
M = [
    [ 0, 10, 10,  1],
    [10,  0,  5,  2],
    [10,  5,  0,  1],
    [ 1,  2,  1,  0]
]

################################################################################

MAX_SUM = -1
SOLUCION = []
SOLUCION_PARCIAL = []
def maxisubconjunto(k, i, suma):
    global N
    global K
    global M
    global MAX_SUM
    global SOLUCION
    global SOLUCION_PARCIAL

    if k > N-i:
        pass
    elif k == 0:
        if suma > MAX_SUM:
            SOLUCION = [val for val in SOLUCION_PARCIAL]
            MAX_SUM = suma
    elif i < N:
        incremento = 0
        for j in SOLUCION_PARCIAL:
            incremento += 2*M[i][j]

        SOLUCION_PARCIAL.append(i)
        maxisubconjunto(k - 1, i + 1, suma + incremento)
        SOLUCION_PARCIAL.pop()
        maxisubconjunto(k, i + 1, suma)

maxisubconjunto(K, 0, 0)
print([1+val for val in SOLUCION])