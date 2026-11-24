# ------- busca por ID --------

def buscar_por_id(inventario, id):

    if id in inventario:
        return inventario[id]
    else:
        return None

# ------ busca linear por nome --------

# busca linear por nome --------
def busca_linear_nome(inventario, valor):
    for id_produto in inventario:
        if valor.lower() == inventario[id_produto][0].lower():
            return inventario[id_produto]
    else:
        return None


# ------- busca por nome --------

def troca(L, i, j):
    L[i], L[j] = L[j], L[i]


def seleciona(L: list, n: int) -> int:
    m = 0
    for i in range(1, n):
        if L[i][1].lower() >= L[m][1].lower():
            m = i
    return m


def selection_sort(L: list):
    n = len(L)  # Define o tamanho da parte não ordenada da lista.
    while n > 1:
        m = seleciona(L, n)
        troca(L, m, n-1)  # Move o elemento com o maior nome alfabeticamente para o final da parte não ordenada.
        n -= 1  # Diminui o tamanho da parte não ordenada, pois o último elemento já está na posição correta.


def busca_binaria(Lista, x):

    x = x.lower()
    inicial = 0
    final = len(Lista) - 1

    while inicial <= final:
        meio = (inicial + final) // 2
        if x == Lista[meio][1].lower():
            return Lista[meio]
        elif x < Lista[meio][1].lower():
            final = meio - 1
        else:
            inicial = meio + 1
    return None


# ----- ordenação para mais de 100 itens -------

def intercala(esquerda: list, direita: list) -> list:
    resultado = []
    i = 0  # Indica a posição atual na metade esquerda da lista.
    j = 0  # Indica a posição atual na metade direita da lista.

    # Compara os elementos enquanto houver itens nas duas metades.
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][1].lower() <= direita[j][1].lower():  # Compara os nomes dos produtos para manter a ordem alfabética.
            resultado.append(esquerda[i])
            i += 1  # Avança para o próximo elemento da metade esquerda.
        else:
            resultado.append(direita[j])
            j += 1  # Avança para o próximo elemento da metade direita.

    # Adiciona ao resultado os elementos que sobraram em qualquer uma das duas metades.
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def merge_sort(lista: list) -> list:
    # Caso base: uma lista com zero ou um elemento já está ordenada.
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio e ordena cada metade recursivamente.
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])  # Seleciona os elementos da metade esquerda da lista.
    direita = merge_sort(lista[meio:])  # Seleciona os elementos da metade direita da lista.

    # Junta as duas metades que já foram ordenadas.
    return intercala(esquerda, direita)


if tipo == 1: 
    resultado = buscar_por_id(inventario, valor)

elif tipo == 2:

    if len(inventario) < 21:
        resultado = busca_linear_nome(inventario, valor)

    else:
        lista_produto = []

        # Percorre o inventário e cria uma lista com o ID e as informações de cada produto.
        for id_produto in inventario:
            lista_produto.append([
                id_produto,
                inventario[id_produto][0],
                inventario[id_produto][1],
                inventario[id_produto][2],
                inventario[id_produto][3]
            ])

        # Seleciona o algoritmo de ordenação de acordo com a quantidade de produtos.
        if len(lista_produto) <= 100:
            selection_sort(lista_produto)
        else:
            lista_produto = merge_sort(lista_produto)

        # A lista está ordenada e pronta para realizar a busca binária.
        resultado = busca_binaria(lista_produto, valor)
