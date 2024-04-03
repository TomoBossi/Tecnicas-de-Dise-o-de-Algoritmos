C_input = [2, 4, 7]
L = 10

C_c = tuple(sorted(C_input))
C_d = tuple([0] + sorted(C_input) + [L])

################################################################################

M_c = [[[None for _ in range(L+1)] for _ in range(len(C_c))] for _ in range(len(C_c))]

def ce_c(i, j, l): # Top-down
    global C_c

    if not M_c[i][j][l]:
        if j < i or i < 0 or j >= len(C_c):
            M_c[i][j][l] = float('inf')
        elif j == i:
            M_c[i][j][l] = l
        else:
            n_cortes = j-i+1
            opciones = [None for _ in range(n_cortes)]
            opciones[0] = ce_c(i+1, j, l-C_c[i])
            opciones[-1] = ce_c(i, j-1, C_c[j])
            for idx, k in enumerate(range(i+1, i+n_cortes-1), start=1):
                opciones[idx] = ce_c(i, k, C_c[k]) + ce_c(k, j, l-C_c[k]) - C_c[k]
            M_c[i][j][l] = l + min(opciones)
    return M_c[i][j][l]

# Todas las operaciones son O(1) y se deben completar O(N^2*L) posiciones
# de la matriz de memorización, por lo que la complejidad temporal es O(N^2*L).
# La complejidad espacial está acotada por la altura máxima del árbol de
# llamados, N, y por el tamaño de las estructuras pasadas por referenica,
# M_c y C_c. Considerando que cada llamado ocupa O(1) espacio de memoria,
# esta complejidad es O(N + N + N^2*L) = O(N^2*L)

################################################################################

M_d = [[None for _ in range(len(C_d))] for _ in range(len(C_d))]

def ce_d(i, j): # Top-down
    global C_d

    if not M_d[i][j]:
        if j <= i or i < 0 or j >= len(C_d):
            M_d[i][j] = float('inf')
        elif j == i+1:
            M_d[i][j] = 0
        else:
            n_cortes = j-i-1
            opciones = [None for _ in range(n_cortes)]
            for idx, k in enumerate(range(i+1, i+1+n_cortes)):
                opciones[idx] = ce_d(i, k) + ce_d(k, j)
            M_d[i][j] = C_d[j]-C_d[i] + min(opciones)
    return M_d[i][j]

# Todas las operaciones son O(1) y se deben completar O(N*L) posiciones
# de la matriz de memorización, por lo que la complejidad temporal es O(N*L).
# La complejidad espacial está acotada por la altura máxima del árbol de
# llamados, N, y por el tamaño de las estructuras pasadas por referenica,
# M_c y C_c. Considerando que cada llamado ocupa O(1) espacio de memoria,
# esta complejidad es O(N + N + N*L) = O(N*L)

print(ce_c(0, len(C_c)-1, L))
print(ce_d(0, len(C_d)-1))