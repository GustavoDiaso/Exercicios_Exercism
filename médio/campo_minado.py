import random
import math

def campo_minado(altura = None, largura = None):

    tamanho_do_campo = None

    if altura is None and largura is None:
        tamanho_do_campo = '5x5'
    else:
        if isinstance(altura, int) and isinstance(largura, int):
            tamanho_do_campo = f'{altura}x{largura}'
        else:
            raise ValueError("Valores inválidos de altura e largura. Somente valores inteiros serão aceitos")

    # Vamos criar um campo minado aleatório, com tamanho definido pelo usuário
    campo = []

    for i in range(0, int(tamanho_do_campo[0])):
        campo.append([])
        for j in range(0, int(tamanho_do_campo[2])):
            # A chance de sair uma bomba deve ser de 1 para 4
            campo[i].append(random.choice(['.', '.', '.', '*']))

    
    # essa função calculará a distancia entre elementos dentro do campo minado
    def distancia_entre_elementos(coordenadas1: list, coordenadas2: list):
        if len(coordenadas1) == 2 and len(coordenadas2) == 2:
            distancia = math.sqrt(((coordenadas2[0]-coordenadas1[0])**2 + (coordenadas2[1]-coordenadas1[1])**2))
            return distancia
        else:
            raise ValueError("Valores de coordenadas inválidos")
    
    for linha_index in range(0, len(campo)):
        for elemento_index in range(0, len(campo[linha_index])):
            # estamos percorrendo cada elemento vazio no campo minado
            if campo[linha_index][elemento_index] != '*':

                # Vamos verificar quantas minas estão ao redor de cada elemento vazio (sem bomba)
                quantidade_de_minas_proximas = 0

                # Quantidade de minas na linha superior (somente a partir da segunda linha)
                if linha_index > 0:
                    try: 
                        for i in range(0, len(campo[linha_index-1])):
                            # Se o elemento for uma bomba, e a distancia entre ele e o elemento que estamos percorrendo for menor que 2, então é uma bomba próxima
                            if campo[linha_index-1][i] == '*' and distancia_entre_elementos([linha_index, elemento_index], [linha_index-1, i]) < 2:
                                quantidade_de_minas_proximas += 1

                    except:
                        ...


                # Quantidade de minas na mesma linha
                try: 
                    for i in range(0, len(campo[linha_index])):
                        # Se o elemento for uma bomba, e a distancia entre ele e o elemento que estamos percorrendo for menor que 2, então é uma bomba próxima
                        if campo[linha_index][i] == '*' and distancia_entre_elementos([linha_index, elemento_index], [linha_index, i]) < 2:
                            quantidade_de_minas_proximas += 1

                except:
                    ...

                # Quantidade de minas na linha de baixo
                try: 
                    for i in range(0, len(campo[linha_index+1])):
                        # Se o elemento for uma bomba, e a distancia entre ele e o elemento que estamos percorrendo for menor que 2, então é uma bomba próxima
                        if campo[linha_index+1][i] == '*' and distancia_entre_elementos([linha_index, elemento_index], [linha_index+1, i]) < 2:
                            quantidade_de_minas_proximas += 1

                except:
                    ...               

                
                # Vamos substituir os elementos vazios pelo número de bombas próximas a eles
                campo[linha_index][elemento_index] = quantidade_de_minas_proximas

    
    """
    Ao final de tudo, teremos um campo parecido com isso:
    [
        [*, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    
    ]

    """
    # Precisamos montar um campo "mascara" que será mostrado ao usuário. Conforme ele escolhe posições, o jogo vai sendo liberado
    # Caso ele escolha uma boma, o jogo acaba.

    
    campo_mascara = []
    # A função map executa uma callback para cada elemento do nosso iterável, retornando um novo iterável cujo valores originais são substituídos 
    # pelo retorno da função

    for linha in campo:
        campo_mascara.append(list(map(lambda x: '🟫', linha)))


    for linha in campo:
        print(*linha)
    # Vamos começar o jogo capturando a escolha de coordenadas do usuário
    # O jogo acaba quando o total de jogadas_restantes é igual ao número total de bombas

    total_de_bombas = 0
    for linha in campo:
        for elemento in linha:
            if elemento == '*':
                total_de_bombas += 1


    jogadas_restantes = (len(campo) * len(campo[0])) - total_de_bombas
    
    while True:

        
        if jogadas_restantes == 0:
            print("-----------------------", '\n Bom jogo!!!!')
            for i in range(0, len(campo_mascara)):
                for j in range(0, len(campo_mascara[i])):
                    if campo_mascara[i][j] == '🟫':
                        campo_mascara[i][j] = '💣'

            print()
            for linha in campo_mascara:
                print(*linha)

            print("\n PARABÉNS, VOCÊ GANHOU O JOGO!!!!")
            break

        print("\nEm qual coordenada devemos pisar?")
        
        print('\n')
        for linha in campo_mascara:
            print(*linha)
        print('\n')

        coordenada_x = None
        coordenada_y = None
        
        while True:
            coordenada_x = input('X: ')
            coordenada_y = input('Y: ')

            try:
                coordenada_x = int(coordenada_x)
                coordenada_y = int(coordenada_y)
                
                # Se a coordenada x fornecida estiver dentro dos padrões
                if coordenada_x >= 0 and coordenada_x < len(campo_mascara):
                    # Se a coordenada y forecida também estiver dentro dos padrões
                    if coordenada_y >= 0 and coordenada_y < len(campo_mascara[coordenada_y]):
                        break

            except ValueError:
                print("Os valores de coordenadas fornecidos são inválidos \n")
        

        if campo[coordenada_x][coordenada_y] != '*':
            campo_mascara[coordenada_x][coordenada_y] = campo[coordenada_x][coordenada_y]
            jogadas_restantes -= 1
            

        else:
            campo_mascara[coordenada_x][coordenada_y] = '💣'
            print('\n')
            for linha in campo_mascara:
                print(*linha)
            print('\n')

            print("Você perdeu!!!!")

            break



campo_minado(2, 2)