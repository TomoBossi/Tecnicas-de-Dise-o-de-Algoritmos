W = [19,  7,  5,  6,  1]
S = [15, 13,  7,  8,  2]
n = len(W)
s_max = max(S)

################################################################################

M = [[None for _ in range(s_max+1)] for _ in range(n)]
M_inf = [None for _ in range(n)]                                                # Memorización para caso especial

def pc(i, s_min): # Top-down
    global W
    global S
    global n

    if i >= n or s_min <= 0:
        return 0
    elif s_min == float('inf'):
        if not M_inf[i]:
            M_inf[i] = max(1 + pc(i+1, S[i]), pc(i+1, s_min))
        return M_inf[i]
    elif not M[i][s_min]:
        M[i][s_min] = max(1 + pc(i+1, min(s_min-W[i], S[i])), pc(i+1, s_min))
    return M[i][s_min]

print(pc(0, float('inf')))

# Todas las operaciones son O(1) y se calculan a lo sumo las N*max{S}+1
# posiciones de la matriz de memorización más las N del vector de memorización
# para el caso especial de s_min = +inf, por lo que la complejidad temporal
# es O(N*max{S}). La complejidad espacial es la de las esctructuras 
# (O(N*max{S})) sumada a la altura máxima del árbol de llamados recursivos 
# (O(N)), por lo que esta complejidad es también O(N*max{S}).