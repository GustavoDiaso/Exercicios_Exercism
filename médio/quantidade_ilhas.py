def qtd_ilhas(matriz: list[list[int]]) -> int:
    num_ilhas:int = 0 
    terreno_de_ilha:list[tuple] = []
    inicio_de_ilha:list[tuple] = []

    for index_linha in range(len(matriz)):
        for index_coluna in range(len(matriz[index_linha])):

            if matriz[index_linha][index_coluna] == 1:

                if (index_linha-1, index_coluna) not in terreno_de_ilha:
                    num_ilhas += 1
                    inicio_de_ilha.append((index_linha, index_coluna))


                for j in range(index_coluna, len(matriz[index_linha])):
                    if matriz[index_linha][j] == 0:
                        break
                    else:
                        terreno_de_ilha.append((index_linha, j))
                        matriz[index_linha][j] = 0

    
                
    print(num_ilhas)


qtd_ilhas([[1,0,1,0,0],[1,0,0,0,1],[1,1,0,0,0],[1,0,1,1,0]])

