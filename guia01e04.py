N = 4
D = [
    [ 0,  1, 10, 10],
    [10,  0,  3, 15],
    [21, 17,  0,  2],
    [ 3, 22, 30,  0]
]

################################################################################

MIN_SUM = sum([sum(row) for row in D])
SOLUCION = []
SOLUCION_PARCIAL = [0]                                                          # SOLUCION_PARCIAL = []
FALTANTES = [False] + [True for _ in range(N-1)]                                # FALTANTES = [True for _ in range(N)]
def rutaminima(k):
    global N
    global D
    global MIN_SUM
    global SOLUCION
    global SOLUCION_PARCIAL
    global FALTANTES

    def evaluar_solucion_candidata(sc):
        return D[sc[N-1]][sc[0]] + sum([D[sc[i]][sc[i+1]] for i in range(N-1)]) # O(N)

    if k == 0:
        suma = evaluar_solucion_candidata(SOLUCION_PARCIAL)                     # O(N)
        if suma < MIN_SUM:                                                      # O(1)
            SOLUCION = [val for val in SOLUCION_PARCIAL]                        # O(N)
            MIN_SUM = suma                                                      # O(1)
    elif len(SOLUCION_PARCIAL) < N:                                             # O(1)
        for i, falta in enumerate(FALTANTES):                                   # O(1)
            if falta:                                                           # O(1)
                SOLUCION_PARCIAL.append(i)                                      # O(1)
                FALTANTES[i] = False                                            # O(1)
                rutaminima(k - 1)                                               # recursión
                SOLUCION_PARCIAL.pop()                                          # O(1)
                FALTANTES[i] = True                                             # O(1)

rutaminima(N-1)                                                                 # rutaminima(N)
print([1+val for val in SOLUCION])