B = [2, 3, 5, 10, 20, 20]
C = 14

################################################################################

def min_soluciones_candidatas(sc1, sc2):
    c1, q1 = sc1
    c2, q2 = sc2
    if c1 < c2:
        return sc1
    elif c1 > c2:
        return sc2
    else:
        if q1 <= q2:
            return sc1
        else:
            return sc2

def incrementar_contador(sc):
    return (sc[0], 1+sc[1])

################################################################################

def cc_b(B, i, k):
    global C

    if k <= 0:
        return (C-k, 0)
    elif i >= 0:
        next_value = B.pop(i)
        rec1 = incrementar_contador(cc_b(B, i-1, k-next_value))
        B.insert(i, next_value)
        rec2 = cc_b(B, i-1, k)
        return min_soluciones_candidatas(rec1, rec2)
    else:
        return (float('inf'), 0)

################################################################################

def cc_c(i, k):
    global B
    global C

    if k <= 0:
        return (C-k, 0)
    elif i >= 0:
        rec1 = incrementar_contador(cc_c(i-1, k-B[i]))
        rec2 = cc_c(i-1, k)
        return min_soluciones_candidatas(rec1, rec2)
    else:
        return (float('inf'), 0)

# Hay escencialmente #B*C = N*K subproblemas posibles (parámetros posibles 
# para cc_c). Hay superposición se pueden llegar a los mismos valores de k 
# usando múltiples combinaciones de billetes distintas, por ej si un valor
# de billete se repite muchas veces en alguna parte de B.

################################################################################

M = [[None for _ in range(C+1)] for _ in range(len(B))] # Matriz N*K

def cc_d(i, k):
    global B
    global C
    global M

    if k <= 0:
        return (C-k, 0)
    elif i >= 0:
        if not M[i][k]:
            rec1 = incrementar_contador(cc_c(i-1, k-B[i]))
            rec2 = cc_c(i-1, k)
            M[i][k] = min_soluciones_candidatas(rec1, rec2)                     # Llamada recursiva que resuelve el problema
        return M[i][k]
    else:
        return (float('inf'), 0)

# Todas las operaciones son O(1) y se tienen que calcular a lo sumo todos los
# N*K valores de la matriz de memorización. Por lo tanto la complejidad temporal
# de peor caso del algoritmo es O(N*K) (O(#B*C))

################################################################################

# print(cc_b(B, len(B)-1, C))
# print(cc_c(len(B)-1, C))
print(cc_d(len(B)-1, C))