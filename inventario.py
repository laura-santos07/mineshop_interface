import busca_e_ordenacao as busca
from pathlib import Path
from criptografia import cifrar_cesar, chave_cesar

# Manipulação do inventário em memória

def adicionar_produto(inventario, dados):
    codigo = dados[0]
    if codigo in inventario:
        return False
    produto = [dados[1], dados[2], round(dados[3], 2), dados[4], dados[5]]
    if encontrar_item(inventario, produto) is not None:
        return False
    inventario[codigo] = produto
    return True


def remover_produto(inventario, codigo):
    if codigo in inventario:
        del inventario[codigo]
        return True
    return False


def atualizar_produto(inventario, dados):
    codigo = dados[0]
    campo = dados[1]
    novo_valor = dados[2]
    if codigo in inventario and 1 <= campo <= 4:
        produto = inventario[codigo][:]
        produto[campo - 1] = novo_valor
        if campo == 3:
            produto[2] = round(novo_valor, 2)
        if campo == 4:
            produto[4] = dados[3]
        for outro in inventario:
            if outro != codigo and mesmo_item(inventario[outro], produto):
                return False
        inventario[codigo] = produto
        return True
    return False


# Exibe listas em páginas de 10 registros.
def paginar(linhas, negociacao=False, texto_escolha="Escolher item para negociação", ordenadas=None):
    if len(linhas) == 0:
        print('Nenhum produto cadastrado.')
        input('Pressione ENTER para voltar ao menu...')
        return False

    originais = linhas
    ordem_alfabetica = False
    por_pagina = 10
    pagina = 1
    total_paginas = (len(linhas) + por_pagina - 1) // por_pagina

    while True:
        inicio = (pagina - 1) * por_pagina
        fim = inicio + por_pagina

        print('━' * 60)
        print(f'Página {pagina} de {total_paginas} | {len(linhas)} produtos')
        print('━' * 60)

        for linha in linhas[inicio:fim]:
            print(linha)

        print('━' * 60)
        print('N - Próxima página | P - Página anterior | V - Voltar ao menu')
        print('I - Primeira página | F - Última página | G - Ir para página')
        if ordenadas is not None:
            print('O - Alternar ordem original / alfabética')
        if negociacao:
            print('C - ' + texto_escolha)

        opcao = input('▷ Escolha uma opção: ').strip().lower()

        if opcao == 'n':
            if pagina < total_paginas:
                pagina += 1
            else:
                print('Você já está na última página.')
        elif opcao == 'p':
            if pagina > 1:
                pagina -= 1
            else:
                print('Você já está na primeira página.')
        elif opcao == 'i':
            pagina = 1
        elif opcao == 'f':
            pagina = total_paginas
        elif opcao == 'g':
            destino = input('▷ Número da página (V para cancelar): ').strip().lower()
            if destino != 'v':
                try:
                    numero = int(destino)
                    if 1 <= numero <= total_paginas:
                        pagina = numero
                    else:
                        print('Página inexistente.')
                except ValueError:
                    print('Informe um número inteiro válido.')
        elif opcao == 'o' and ordenadas is not None:
            if ordem_alfabetica == False:
                linhas = ordenadas
                ordem_alfabetica = True
            else:
                linhas = originais
                ordem_alfabetica = False
            pagina = 1
        elif opcao == 'v':
            return False
        elif opcao == 'c' and negociacao:
            return True
        else:
            print('Opção inválida.')


def formatar_produto(codigo, produto):
    encantamento = produto[4]
    if encantamento == "":
        encantamento = "Nenhum"
    return f'ID: {codigo} | Nome: {produto[0]} | Quantidade: {produto[1]} | Preço: {produto[2]:.2f} | Encantado: {produto[3]} | Encantamento: {encantamento}'


def mostrar_produtos(inventario, negociacao=False, texto_escolha="Escolher item para negociação", disponibilidade=None):
    linhas = []
    linhas_ordenadas = []
    por_id = {}
    for codigo in inventario:
        produto = inventario[codigo]
        linha = formatar_produto(codigo, produto)
        if disponibilidade is not None:
            linha += f' | Disponível para venda: {disponibilidade[codigo]}'
        linhas.append(linha)
        por_id[codigo] = linha
    for registro in busca.ordenar_produtos(inventario):
        linhas_ordenadas.append(por_id[registro[0]])
    return paginar(linhas, negociacao, texto_escolha, linhas_ordenadas)


def mostrar_estatisticas(inventario):
    total = 0
    quantidade = 0
    for codigo in inventario:
        produto = inventario[codigo]
        quantidade += produto[1]
        total += produto[1] * produto[2]
    print(f'Produtos cadastrados: {len(inventario)}')
    print(f'Total de unidades: {quantidade}')
    print(f'Valor total do estoque: {total:.2f} esmeraldas')


# Carrega os dados para um dicionário. None indica erro de leitura.
def carregar_inventario(nome_arquivo="inventario.csv"):
    inventario = {}
    numero = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                numero += 1
                if linha.strip() == '':
                    continue
                dados_cifrados = linha.rstrip('\r\n').split(';')
                dados = [cifrar_cesar(campo, -chave_cesar) for campo in dados_cifrados]
                if len(dados) != 6:
                    print(f'▷ {nome_arquivo}, linha {numero}: esperados seis campos.')
                    return None
                codigo = int(dados[0])
                nome = dados[1].strip()
                quantidade = int(dados[2])
                preco = float(dados[3])
                if codigo < 0 or codigo in inventario or nome == '' or quantidade < 0 or not 0 <= preco < float('inf') or preco != round(preco, 2):
                    print(f'▷ {nome_arquivo}, linha {numero}: dados inválidos ou ID duplicado.')
                    return None
                if dados[4] != 'True' and dados[4] != 'False':
                    print(f'▷ {nome_arquivo}, linha {numero}: booleano inválido.')
                    return None
                encantado = dados[4] == 'True'
                encantamento = dados[5].strip()
                if (encantado and encantamento == '') or (not encantado and encantamento != ''):
                    print(f'▷ {nome_arquivo}, linha {numero}: encantamento inconsistente.')
                    return None
                produto = [nome, quantidade, preco, encantado, encantamento]
                if encontrar_item(inventario, produto) is not None:
                    print(f'▷ {nome_arquivo}, linha {numero}: produto duplicado.')
                    return None
                inventario[codigo] = produto
    except FileNotFoundError:
        if nome_arquivo == "inventario.csv":
            print('▷ O arquivo inventario.csv não foi encontrado.')
            resposta = input('▷ Criar um inventário vazio? (S/N): ').strip().lower()
            if resposta == 's' or resposta == 'sim':
                try:
                    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                        pass
                    print('▷ Inventário vazio criado com sucesso.')
                    return {}
                except OSError:
                    print('▷ Não foi possível criar inventario.csv.')
                    return None
            print('▷ Coloque o arquivo na pasta e execute o programa novamente.')
            return None
        print(f'▷ Não foi possível abrir {nome_arquivo}. Confira a pasta do projeto.')
        return None
    except OSError:
        print(f'▷ Não foi possível abrir {nome_arquivo}. Confira a pasta do projeto.')
        return None
    except ValueError:
        print(f'▷ {nome_arquivo}, linha {numero}: dados inválidos.')
        return None
    return inventario


def salvar_inventario(inventario, nome_arquivo="inventario.csv"):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for codigo in inventario:
            produto = inventario[codigo]
            campos = [
                cifrar_cesar(codigo, chave_cesar),
                cifrar_cesar(produto[0], chave_cesar),
                cifrar_cesar(produto[1], chave_cesar),
                cifrar_cesar(produto[2], chave_cesar),
                cifrar_cesar(produto[3], chave_cesar),
                cifrar_cesar(produto[4], chave_cesar),
            ]
            arquivo.write(';'.join(campos) + '\n')

def carregar_esmeraldas():
    try:
        with open('esmeraldas.txt', 'r', encoding='utf-8') as arquivo:
            saldo = float(arquivo.read().strip())
            if 0 <= saldo < float('inf') and saldo == round(saldo, 2):
                return saldo
    except OSError:
        print('▷ Não foi possível abrir esmeraldas.txt.')
        return None
    except ValueError:
        print('▷ Saldo de esmeraldas inválido.')
        return None
    print('▷ Saldo de esmeraldas inválido.')
    return None


def salvar_esmeraldas(esmeraldas):
    with open('esmeraldas.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f'{esmeraldas:.2f}\n')


# Dicionário separado: ID do item e quantidade disponível para venda.
def carregar_disponibilidade(jogador):
    disponibilidade = {}
    numero = 0
    try:
        with open('disponibilidade_jogador.csv', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                numero += 1
                if linha.strip() == '':
                    continue
                dados = linha.strip().split(';')
                if len(dados) != 2:
                    print(f'▷ Disponibilidade inválida na linha {numero}.')
                    return None
                codigo = int(dados[0])
                quantidade = int(dados[1])
                if codigo not in jogador or codigo in disponibilidade or quantidade < 0 or quantidade > jogador[codigo][1]:
                    print(f'▷ Disponibilidade inválida na linha {numero}.')
                    return None
                disponibilidade[codigo] = quantidade
    except OSError:
        print('▷ Não foi possível abrir disponibilidade_jogador.csv.')
        return None
    except ValueError:
        print(f'▷ Disponibilidade inválida na linha {numero}.')
        return None
    if len(disponibilidade) != len(jogador):
        print('▷ Faltam itens no arquivo de disponibilidade.')
        return None
    return disponibilidade


def salvar_disponibilidade(disponibilidade):
    with open('disponibilidade_jogador.csv', 'w', encoding='utf-8') as arquivo:
        for codigo in disponibilidade:
            arquivo.write(f'{codigo};{disponibilidade[codigo]}\n')


def definir_disponibilidade(jogador, disponibilidade, codigo, quantidade):
    if codigo not in jogador or quantidade < 0 or quantidade > jogador[codigo][1]:
        return 'ID ou quantidade disponível inválida.'
    disponibilidade[codigo] = quantidade
    return 'Quantidade disponível para venda atualizada!'


# Procura um item pelo nome e encantamento, sem confundir IDs de inventários.
def mesmo_item(item, produto):
    return item[0].strip().lower() == produto[0].strip().lower() and item[3] == produto[3] and item[4].strip().lower() == produto[4].strip().lower()


def encontrar_item(inventario, produto):
    for codigo in inventario:
        item = inventario[codigo]
        if mesmo_item(item, produto):
            return codigo
    return None


def receber_item(inventario, produto, quantidade, disponibilidade):
    codigo = encontrar_item(inventario, produto)
    if codigo is None:
        codigo = 1
        while codigo in inventario:
            codigo += 1
        inventario[codigo] = [produto[0], quantidade, produto[2], produto[3], produto[4]]
        disponibilidade[codigo] = 0
    else:
        inventario[codigo][1] += quantidade
        inventario[codigo][2] = produto[2]


def comprar_item(loja, jogador, esmeraldas, codigo, quantidade, disponibilidade):
    if codigo not in loja or quantidade <= 0:
        return esmeraldas, 'Produto ou quantidade inválida.'
    produto = loja[codigo]
    custo = round(produto[2] * quantidade, 2)
    if quantidade > produto[1]:
        return esmeraldas, 'Estoque insuficiente.'
    if custo > esmeraldas:
        return esmeraldas, 'Esmeraldas insuficientes.'
    receber_item(jogador, produto, quantidade, disponibilidade)
    produto[1] -= quantidade
    return round(esmeraldas - custo, 2), 'Compra realizada com sucesso!'


def vender_item(loja, jogador, esmeraldas, codigo, quantidade, disponibilidade):
    if codigo not in jogador or quantidade <= 0:
        return esmeraldas, 'Produto ou quantidade inválida.'
    produto = jogador[codigo]
    if quantidade > produto[1]:
        return esmeraldas, 'Você não possui essa quantidade.'
    codigo_loja = encontrar_item(loja, produto)
    if codigo_loja is None:
        return esmeraldas, 'Venda não permitida: o item não está cadastrado no Villager.'
    if quantidade > disponibilidade[codigo]:
        return esmeraldas, 'Quantidade disponível para venda insuficiente.'
    # Usa o preço atual definido pelo administrador.
    ganho = round(loja[codigo_loja][2] * quantidade, 2)
    loja[codigo_loja][1] += quantidade
    produto[1] -= quantidade
    disponibilidade[codigo] -= quantidade
    if produto[1] == 0:
        del jogador[codigo]
        del disponibilidade[codigo]
    return round(esmeraldas + ganho, 2), 'Venda realizada com sucesso!'


# Cadastra um item no inventário pessoal, mesmo sem oferta na loja.
def coletar_item(loja, jogador, dados, disponibilidade):
    nome = dados[0]
    quantidade = dados[1]
    encantado = dados[2]
    encantamento = dados[3]
    if nome.strip() == '' or ';' in nome or quantidade <= 0:
        return 'Produto ou quantidade inválida.'
    # O jogador não define o preço. Sem oferta, o item ainda não pode ser vendido.
    produto = [nome, quantidade, 0.0, encantado, encantamento]
    codigo_loja = encontrar_item(loja, produto)
    if codigo_loja is not None:
        produto[2] = loja[codigo_loja][2]
    receber_item(jogador, produto, quantidade, disponibilidade)
    if codigo_loja is None:
        return 'Item coletado com sucesso! Venda disponível quando o Villager cadastrar uma oferta.'
    return 'Item coletado com sucesso!'


# Mantém o preço exibido no inventário pessoal igual ao preço da loja.
def atualizar_precos_jogador(loja, jogador):
    for codigo in jogador:
        codigo_loja = encontrar_item(loja, jogador[codigo])
        if codigo_loja is not None:
            jogador[codigo][2] = loja[codigo_loja][2]
        else:
            jogador[codigo][2] = 0.0


# Exibe o preço vigente e informa quais itens podem ser vendidos.
def mostrar_itens_venda(loja, jogador, disponibilidade):
    linhas = []
    for codigo in jogador:
        produto = jogador[codigo]
        codigo_loja = encontrar_item(loja, produto)
        if codigo_loja is None:
            situacao = 'Sem oferta - não pode vender'
        else:
            situacao = f'Preço de venda: {loja[codigo_loja][2]:.2f} esmeraldas'
        disponivel = disponibilidade[codigo]
        linhas.append(f'ID: {codigo} | Nome: {produto[0]} | Quantidade: {produto[1]} | Disponível: {disponivel} | Encantamento: {produto[4] or "Nenhum"} | {situacao}')
    return paginar(linhas, True)


def remover_item_jogador(jogador, codigo, quantidade, disponibilidade):
    if codigo not in jogador or quantidade <= 0:
        return 'Produto ou quantidade inválida.'
    if quantidade > jogador[codigo][1]:
        return 'Você não possui essa quantidade.'
    jogador[codigo][1] -= quantidade
    if disponibilidade[codigo] > jogador[codigo][1]:
        disponibilidade[codigo] = jogador[codigo][1]
    if jogador[codigo][1] == 0:
        del jogador[codigo]
        del disponibilidade[codigo]
    return 'Item removido com sucesso!'
