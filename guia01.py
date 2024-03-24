from copy import deepcopy

def cuantos_cuadrados_magicos(n, cuadrado, i, j, numeros):

    def es_cuadrado_magico(n, cuadrado):
        res = True
        for i in range(n):
            res = res and sum(cuadrado[i]) == sum([cuadrado[j][i] for j in range(n)]) == (n**3 + n)/2
        res = res and sum([cuadrado[i][i] for i in range(n)]) == sum([cuadrado[i][n-1-i] for i in range(n)]) == (n**3 + n)/2
        return res
        
    if i == n:
        if es_cuadrado_magico(n, cuadrado):
            print(cuadrado)
            return True
        return False

    res = 0
    prox_i = i
    prox_j = j + 1
    if j == n-1:
        prox_i += 1
        prox_j = 0

    suma_fila = sum(cuadrado[i])
    suma_columna = sum([cuadrado[k][j] for k in range(n)])

    for numero in numeros:
        fila_invalida = (suma_fila + numero) > int((n**3 + n)/2)
        columna_invalida = (suma_columna + numero) > int((n**3 + n)/2)
        if not fila_invalida and not columna_invalida:
            cuadrado[i][j] = numero
            res += cuantos_cuadrados_magicos(n, cuadrado, prox_i, prox_j, numeros - {numero})
    cuadrado[i][j] = 0 # BACKTRACKING
    return res

print(cuantos_cuadrados_magicos(3, [[0,0,0],[0,0,0],[0,0,0]], 0, 0, {1,2,3,4,5,6,7,8,9}))