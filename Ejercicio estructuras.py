n = 2

m = 2

 

matriz = [[0] * m for i in range(n)] #llenamos la matriz de ceros

 

fila_inicio = 0

fila_fin = n-1

columna_inicio = 0

columna_fin = m-1

valor = 1

 

while fila_inicio <= fila_fin and columna_inicio <= columna_fin:

 

    for i in range(fila_inicio, fila_fin+1):

        matriz[i][columna_inicio] = valor

        valor += 1

 

    for j in range(columna_inicio+1, columna_fin+1):

        matriz[fila_fin][j] = valor

        valor += 1

 

    if fila_inicio < fila_fin:

        for i in range(fila_fin-1, fila_inicio-1, -1):

            matriz[i][columna_fin] = valor

            valor += 1

 

    if columna_inicio < columna_fin:

        for j in range(columna_fin-1, columna_inicio, -1):

            matriz[fila_inicio][j] = valor

            valor += 1

 

    fila_inicio += 1

    fila_fin -= 1

    columna_inicio += 1

    columna_fin -= 1

 

for fila in matriz:

    print(fila)