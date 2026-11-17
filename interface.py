def menu():
    print('━' * 60)
    print('▣ MENU PRINCIPAL - MINESHOP')
    print('━' * 60)
    villager()
    print('━' * 60)
    print('▷ Adicionar produto (1)')
    print('▷ Remover produto (2)')
    print('▷ Atualizar produto (3)')
    print('▷ Buscar produto (4)')
    print('▷ Mostrar produtos (5)')
    print('▷ Estatísticas (6)')
    print('▷ Alterar login (7)')
    print('▷ Salvar e sair (8)')
    print('━' * 60)

def villager():
    print('    ░░░░░░░░░░░░░░')
    print('    ░░▒▒▒▒▒▒▒▒▒▒░░')
    print('    ░░▒▒▒▒▒▒▒▒▒▒░░')
    print('    ░░██████████░░')
    print('    ░░██░▓▒▒▓░██░░')
    print('    ░░▒▒▒████▒▒▒▒░')
    print('    ░░▒▒░████░▒▒░░')
    print('    ░░▒▒░████░▒▒░░')

def escolher_opcao():
    opcao = validar_itens('▷ Escolha uma opção: ')

    while opcao < 1 or opcao > 8:
        print('⚠ Erro: Escolha uma opção de 1 a 8.')
        opcao = validar_itens('▷ Escolha uma opção: ')

    return opcao

def validar_itens(mensagem):
    while True: # Repete a pergunta até receber um número válido
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print('⚠ Erro: Insira um número não negativo.')
            else:
                return valor

        except ValueError:
            print('⚠ Erro: Insira um número inteiro válido.')

def validar_compra(mensagem):
    while True:
        resposta = input(mensagem).strip()

        if resposta == 'Sim' or resposta == 'sim' or resposta == 'SIM':
            return True

        elif resposta == 'Não' or resposta == 'não' or resposta == 'Nao' or resposta == 'nao' or resposta == 'NÃO' or resposta == 'NAO':
            return False

        else:
            print('⚠ Erro: Responda Sim ou Não.')

def validar_decimal(mensagem): # Valida os valores decimais dos produtos
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0 or valor != valor or valor == float('inf') or valor == float('-inf'):
                print('⚠ Erro: Insira um valor válido e não negativo.')
            else:
                return valor

        except ValueError:
            print('⚠ Erro: Insira um número válido.')

def validar_nome(mensagem): # Impede que o nome do produto fique vazio
    while True:
        nome = input(mensagem).strip()

        if nome == '':
            print('⚠ Erro: Digite o nome do produto.')
        else:
            return nome

def validar_id(mensagem, inventario): # Confere se o ID já está sendo usado
    while True:
        codigo = validar_itens(mensagem)

        if codigo in inventario:
            print('⚠ Erro: Esse ID já está cadastrado.')
        else:
            return codigo

def validar_id_existente(mensagem, inventario): # Confere se o produto existe antes de alterar ou remover
    while True:
        codigo = validar_itens(mensagem)

        if codigo in inventario:
            return codigo
        else:
            print('⚠ Erro: Produto não encontrado.')

def validar_importado(mensagem): # Recebe Sim ou Não para indicar se o item é importado
    return validar_compra(mensagem)

# TELA PARA ADICIONAR O PRODUTO
def adicionar_produto():
    print('━' * 60)
    print('▣ MINESHOP - ADICIONAR PRODUTO')
    print('━' * 60)

    codigo = validar_itens('▷ ID do produto: ')
    nome = validar_nome('▷ Nome do produto: ')
    quantidade = validar_itens('▷ Quantidade: ')
    preco = validar_decimal('▷ Preço: ')
    importado = validar_importado('▷ Produto importado? (Sim/Não): ')

    print('━' * 60)
    print('▷ Dados preenchidos. O cadastro será feito na integração.')
    return [codigo, nome, quantidade, preco, importado]


# TELA PARA REMOVER O PRODUTO
def remover_produto():
    print('━' * 60)
    print('▣ MINESHOP - REMOVER PRODUTO')
    print('━' * 60)

    codigo = validar_itens('▷ ID do produto que deseja remover: ')
    confirmar = validar_compra('▷ Confirmar remoção? (Sim/Não): ')

    print('━' * 60)
    if confirmar:
        print('▷ Pedido de remoção preenchido. Nenhum produto foi removido.')
        return codigo
    else:
        print('▷ Remoção cancelada.')
        return


# TELA PARA ATUALIZAR O PRODUTO
def atualizar_produto():
    print('━' * 60)
    print('▣ MINESHOP - ATUALIZAR PRODUTO')
    print('━' * 60)

    codigo = validar_itens('▷ ID do produto que deseja atualizar: ')
    print('▷ Nome (1)')
    print('▷ Quantidade (2)')
    print('▷ Preço (3)')
    print('▷ Importado (4)')

    campo = validar_itens('▷ O que deseja atualizar? ')
    while campo < 1 or campo > 4:
        print('⚠ Erro: Escolha uma opção de 1 a 4.')
        campo = validar_itens('▷ O que deseja atualizar? ')

    if campo == 1:
        novo_valor = validar_nome('▷ Novo nome: ')
    elif campo == 2:
        novo_valor = validar_itens('▷ Nova quantidade: ')
    elif campo == 3:
        novo_valor = validar_decimal('▷ Novo preço: ')
    else:
        novo_valor = validar_importado('▷ Produto importado? (Sim/Não): ')

    print('━' * 60)
    print('▷ Dados preenchidos. A atualização será feita na integração.')
    return [codigo, campo, novo_valor]


# TELA PARA BUSCAR O PRODUTO
def buscar_produto():
    print('━' * 60)
    print('▣ MINESHOP - BUSCAR PRODUTO')
    print('━' * 60)
    print('▷ Buscar por ID (1)')
    print('▷ Buscar por nome (2)')

    tipo = validar_itens('▷ Escolha uma opção: ')
    while tipo < 1 or tipo > 2:
        print('⚠ Erro: Escolha 1 ou 2.')
        tipo = validar_itens('▷ Escolha uma opção: ')

    if tipo == 1:
        valor = validar_itens('▷ ID do produto: ')
    else:
        valor = validar_nome('▷ Nome do produto: ')

    print('━' * 60)
    print('▷ Busca preenchida. A consulta será feita na integração.')
    return [tipo, valor]


# TELA PARA MOSTRAR OS PRODUTOS
def mostrar_produtos():
    print('━' * 60)
    print('▣ MINESHOP - MOSTRAR PRODUTOS')
    print('━' * 60)
    print('▷ Lista de produtos cadastrados.')
    print('━' * 60)

# TELA PARA ESTATÍSTICAS
def mostrar_estatisticas():
    print('━' * 60)
    print('▣ MINESHOP - ESTATÍSTICAS')
    print('━' * 60)
    print('▷ Quantidade de produtos e valor total do inventário.')
    print('━' * 60)

# TELA PARA ALTERAR LOGIN
def tela_alterar_login():
    print('━' * 60)
    print('▣ MINESHOP - ALTERAR LOGIN')
    print('━' * 60)
    print('▷ Alteração de usuário e senha.')
    print('━' * 60)

# TELA PARA SALVAR E SAIR
def tela_sair():
    print('━' * 60)
    print('▣ MINESHOP - SALVAR E SAIR')
    print('━' * 60)
    print('▷ Encerramento do programa.')
    print('━' * 60)