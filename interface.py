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
        opcao = validar_itens('▷ Escolha uma opção: ') # Executa novamente a função validar_itens() e substitui o valor anterior da variável opcao

    return opcao

def validar_itens(mensagem):
    while True: # Mantém a função até que a entrada seja válida
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
        resposta = input(mensagem)

        if resposta == 'Sim' or resposta == 'sim':
            return True

        elif resposta == 'Não' or resposta == 'não' or resposta == 'Nao' or resposta == 'nao':
            return False

        else:
            print('⚠ Erro: Responda Sim ou Não.')

def validar_decimal(mensagem): # Valida os valores decimais dos produtos
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print('⚠ Erro: Insira um valor não negativo.')
            else:
                return valor

        except ValueError:
            print('⚠ Erro: Insira um número válido.')

def validar_nome(mensagem): # Impede que o nome do produto fique vazio
    while True:
        nome = input(mensagem)

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

# TELA PARA ADICIONAR O PRODUTO
def adicionar_produto():
    print('━' * 60)
    print('▣ MINESHOP - ADICIONAR PRODUTO')
    print('━' * 60)
    print('▷ Bem-vindo ao sistema de produtos!')
    print('▷ Aqui serão exibidos os itens disponíveis.')
    print('━' * 60)

# TELA PARA REMOVER O PRODUTO
def remover_produto():
    print('━' * 60)
    print('▣ MINESHOP - REMOVER PRODUTO')
    print('━' * 60)
    print('▷ Aqui você poderá remover produtos do inventário.')
    print('━' * 60)

# TELA PARA ATUALIZAR O PRODUTO
def atualizar_produto():
    print('━' * 60)
    print('▣ MINESHOP - ATUALIZAR PRODUTO')
    print('━' * 60)
    print('▷ Aqui você poderá atualizar as informações dos produtos.')
    print('━' * 60)

# TELA PARA BUSCAR O PRODUTO
def buscar_produto():
    print('━' * 60)
    print('▣ MINESHOP - BUSCAR PRODUTO')
    print('━' * 60)
    print('▷ Aqui você poderá buscar produtos por nome ou ID.')
    print('━' * 60)