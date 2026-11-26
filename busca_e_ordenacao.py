# ------- busca por ID --------

# Como o ID é a chave do dicionário, a consulta pode ser feita diretamente.
def buscar_por_id(inventario, id):

    if id in inventario:
        return inventario[id]
    else:
        return None

# ------ busca linear por nome --------

# busca linear por nome --------
# Percorre os produtos e aceita tanto nomes exatos quanto buscas por parte do nome.
def busca_linear_nome(inventario, valor, parcial=False):
    resultados = []
    for codigo in inventario:
        nome = inventario[codigo][0].lower()
        if (parcial and valor.lower() in nome) or (not parcial and valor.lower() == nome):
            resultados.append([codigo] + inventario[codigo])
    return resultados


# ------- busca por nome --------

# Auxilia a ordenação trocando dois elementos de posição.
def troca(L, i, j):
    auxiliar = L[i]
    L[i] = L[j]
    L[j] = auxiliar


# Localiza o maior nome da parte ainda não ordenada.
def seleciona(L, n):
    m = 0
    for i in range(1, n):
        if L[i][1].lower() >= L[m][1].lower():
            m = i
    return m


# O Selection Sort é usado em listas menores pela simplicidade de implementação.
def selection_sort(L):
    n = len(L)  # Define o tamanho da parte não ordenada da lista.
    while n > 1:
        m = seleciona(L, n)
        troca(L, m, n-1)  # Move o elemento com o maior nome alfabeticamente para o final da parte não ordenada.
        n -= 1  # Diminui o tamanho da parte não ordenada, pois o último elemento já está na posição correta.


# Com a lista ordenada, descarta metade do intervalo a cada comparação.
def busca_binaria(Lista, x):
    x = x.lower()
    inicial = 0
    final = len(Lista) - 1
    while inicial <= final:
        meio = (inicial + final) // 2
        if x == Lista[meio][1].lower():
            # Encontra todas as variantes com o mesmo nome.
            while meio > 0 and Lista[meio - 1][1].lower() == x:
                meio -= 1
            resultados = []
            while meio < len(Lista) and Lista[meio][1].lower() == x:
                resultados.append(Lista[meio])
                meio += 1
            return resultados
        elif x < Lista[meio][1].lower():
            final = meio - 1
        else:
            inicial = meio + 1
    return []


# ----- ordenação para mais de 100 itens -------

def intercala(esquerda, direita):
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
    for item in esquerda[i:]:
        resultado.append(item)
    for item in direita[j:]:
        resultado.append(item)

    return resultado


# Para listas maiores, a divisão em metades reduz o custo da ordenação em relação ao Selection Sort.
def merge_sort(lista):
    # Caso base: uma lista com zero ou um elemento já está ordenada.
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio e ordena cada metade recursivamente.
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])  # Seleciona os elementos da metade esquerda da lista.
    direita = merge_sort(lista[meio:])  # Seleciona os elementos da metade direita da lista.

    # Junta as duas metades que já foram ordenadas.
    return intercala(esquerda, direita)



# Transforma o dicionário em lista e escolhe o algoritmo pelo limite de 100 produtos.
def ordenar_produtos(inventario):
    lista = []
    for codigo in inventario:
        lista.append([codigo] + inventario[codigo])
    if len(lista) <= 100:
        selection_sort(lista)
    else:
        lista = merge_sort(lista)
    return lista


# A busca por ID é direta; nomes parciais usam busca linear e nomes exatos podem usar busca binária.
def buscar(inventario, tipo, valor):
    if tipo == 1:
        produto = buscar_por_id(inventario, valor)
        if produto is None:
            return []
        return [[valor] + produto]
    if tipo == 3:
        return busca_linear_nome(inventario, valor, True)
    if len(inventario) < 21:
        return busca_linear_nome(inventario, valor)
    return busca_binaria(ordenar_produtos(inventario), valor)
