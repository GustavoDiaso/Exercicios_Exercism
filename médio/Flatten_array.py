"""
Instruções
Pegue uma lista aninhada e retorne uma única lista simplificada com todos os valores, exceto nil/null.

O desafio é pegar uma estrutura aninhada, semelhante a uma lista, arbitrariamente profunda e produzir uma
estrutura simplificada, sem nenhum valor nulo/nil.

Por exemplo:

entrada: [1,[2,3,nulo,4],[nulo],5]

saída: [1,2,3,4,5]
"""
from ftplib import all_errors


def flatten_array(array:list) -> list:

    def has_nest(arr: list) -> bool:
        for i in arr:
            if isinstance(i, list):
                return True

        return False

    # removing every nest
    while has_nest(array):
        new_list = []
        for elem in array:
            if isinstance(elem, list):
                for x in elem:
                    new_list.append(x)

                continue

            new_list.append(elem)

        array = new_list

    # removing every 'None' value
    for index, value in enumerate(array):
        if value is None:
            del array[index]

    return array


print(flatten_array([1,[2,3,None,4,[21,34,None,[32,None, 234]]],[None],5]))


