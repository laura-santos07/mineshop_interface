# ESCOLHA DE PERFIL
# Apresenta os perfis disponíveis antes de abrir o menu de operações.
def menu_inicial():
    print('━' * 60)
    print('▣ BEM-VINDO AO MINESHOP')
    print('━' * 60)
    villager()
    print('━' * 60)
    print('▷ Entrar como Villager - Administrador (1)')
    print('▷ Entrar como Jogador (2)')
    print('▷ Sair (3)')
    print('━' * 60)


# Limita a escolha às opções exibidas no menu inicial.
def escolher_perfil():
    opcao = validar_itens('▷ Escolha uma opção: ')

    while opcao < 1 or opcao > 3:
        print('⚠ Erro: Escolha uma opção de 1 a 3.')
        opcao = validar_itens('▷ Escolha uma opção: ')

    return opcao


# MENU DO JOGADOR
# Reúne as operações de negociação e inventário pessoal.
def menu_jogador():
    print('━' * 60)
    print('▣ MINESHOP - JOGADOR')
    print('━' * 60)
    print('▷ Ver produtos da loja (1)')
    print('▷ Comprar item com esmeraldas (2)')
    print('▷ Vender item por esmeraldas (3)')
    print('▷ Meu inventário (4)')
    print('▷ Coletar item para meu inventário (5)')
    print('▷ Remover item do meu inventário (6)')
    print('▷ Definir quantidade disponível para venda (7)')
    print('▷ Buscar produto (8)')
    print('▷ Voltar ao início (9)')
    print('━' * 60)


# Impede a seleção de opções fora do menu do jogador.
def escolher_opcao_jogador():
    opcao = validar_itens('▷ Escolha uma opção: ')

    while opcao < 1 or opcao > 9:
        print('⚠ Erro: Escolha uma opção de 1 a 9.')
        opcao = validar_itens('▷ Escolha uma opção: ')

    return opcao


# Solicita o ID da loja e a quantidade, permitindo cancelar antes da compra.
def tela_comprar():
    print('━' * 60)
    print('▣ MINESHOP - COMPRAR ITEM')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)
    codigo = validar_itens('▷ ID do produto: ', True)
    if codigo is None:
        return None
    quantidade = validar_itens('▷ Quantidade: ', True)
    if quantidade is None:
        return None
    return codigo, quantidade


# Solicita o ID do inventário pessoal e a quantidade a vender.
def tela_vender():
    print('━' * 60)
    print('▣ MINESHOP - VENDER ITEM')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)
    codigo = validar_itens('▷ ID do seu item: ', True)
    if codigo is None:
        return None
    quantidade = validar_itens('▷ Quantidade: ', True)
    if quantidade is None:
        return None
    return codigo, quantidade


# Identifica a tela de consulta do inventário pessoal.
def tela_inventario_jogador():
    print('━' * 60)
    print('▣ MINESHOP - MEU INVENTÁRIO')
    print('━' * 60)


# Exibe as operações de gerenciamento disponíveis ao Villager.
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
    print('▷ Voltar ao início (0)')
    print('━' * 60)

# Desenha o personagem no terminal sem precisar de uma interface gráfica.
def villager():
    print('    ░░░░░░░░░░░░░░')
    print('    ░░▒▒▒▒▒▒▒▒▒▒░░')
    print('    ░░▒▒▒▒▒▒▒▒▒▒░░')
    print('    ░░██████████░░')
    print('    ░░██░▓▒▒▓░██░░')
    print('    ░░▒▒▒████▒▒▒▒░')
    print('    ░░▒▒░████░▒▒░░')
    print('    ░░▒▒░████░▒▒░░')

# Valida o intervalo de opções do menu administrativo.
def escolher_opcao():
    opcao = validar_itens('▷ Escolha uma opção: ')

    while opcao < 0 or opcao > 8:
        print('⚠ Erro: Escolha uma opção de 0 a 8.')
        opcao = validar_itens('▷ Escolha uma opção: ')

    return opcao

# Aceita inteiros não negativos e permite voltar quando a operação oferece essa opção.
def validar_itens(mensagem, voltar=False):
    while True: # Repete a pergunta até receber um número válido
        try:
            resposta = input(mensagem).strip()
            if voltar and resposta.lower() == 'v':
                return None
            valor = int(resposta)

            if valor < 0:
                print('⚠ Erro: Insira um número não negativo.')
            else:
                return valor

        except ValueError:
            print('⚠ Erro: Insira um número inteiro válido.')

# Converte as respostas de sim ou não em valores booleanos.
def validar_compra(mensagem, voltar=False):
    while True:
        resposta = input(mensagem).strip()
        if voltar and resposta.lower() == 'v':
            return None

        if resposta == 'Sim' or resposta == 'sim' or resposta == 'SIM':
            return True

        elif resposta == 'Não' or resposta == 'não' or resposta == 'Nao' or resposta == 'nao' or resposta == 'NÃO' or resposta == 'NAO':
            return False

        else:
            print('⚠ Erro: Responda Sim ou Não.')

# Recusa valores negativos ou não finitos e limita o preço a duas casas decimais.
def validar_decimal(mensagem, voltar=False): # Valida os valores decimais dos produtos
    while True:
        try:
            resposta = input(mensagem).strip()
            if voltar and resposta.lower() == 'v':
                return None
            valor = float(resposta)

            if not 0 <= valor < float('inf'):
                print('⚠ Erro: Insira um valor válido e não negativo.')
            else:
                return round(valor, 2)

        except ValueError:
            print('⚠ Erro: Insira um número válido.')

# Também impede o uso do ponto e vírgula, pois ele separa os campos no CSV.
def validar_nome(mensagem, voltar=False): # Impede que o nome do produto fique vazio
    while True:
        nome = input(mensagem).strip()
        if voltar and nome.lower() == 'v':
            return None

        if nome == '':
            print('⚠ Erro: Digite o nome do produto.')
        elif ';' in nome:
            print('⚠ Erro: O nome não pode conter ponto e vírgula.')
        else:
            return nome

def validar_id(mensagem, inventario): # Confere se o ID já está sendo usado
    while True:
        codigo = validar_itens(mensagem, True)
        if codigo is None:
            return None

        if codigo in inventario:
            print('⚠ Erro: Esse ID já está cadastrado.')
        else:
            return codigo

def validar_id_existente(mensagem, inventario): # Confere se o produto existe antes de alterar ou remover
    while True:
        codigo = validar_itens(mensagem, True)
        if codigo is None:
            return None

        if codigo in inventario:
            return codigo
        else:
            print('⚠ Erro: Produto não encontrado.')

# Usa uma lista de encantamentos para apresentar escolhas padronizadas.
def escolher_encantamento():
    encantamentos = ['Afiação', 'Proteção', 'Eficiência', 'Inquebrável',
                     'Remendo', 'Fortuna', 'Toque suave', 'Pilhagem',
                     'Aspecto flamejante', 'Repulsão', 'Força', 'Chama',
                     'Infinidade', 'Queda suave', 'Espinhos', 'Respiração']
    print('━' * 60)
    print('▣ MINESHOP - ENCANTAMENTOS')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)
    for i in range(len(encantamentos)):
        print(f'▷ {encantamentos[i]} ({i + 1})')
    opcao = validar_itens('▷ Escolha o encantamento: ', True)
    if opcao is None:
        return None
    while opcao < 1 or opcao > len(encantamentos):
        print('⚠ Erro: Escolha uma opção válida.')
        opcao = validar_itens('▷ Escolha o encantamento: ', True)
        if opcao is None:
            return None
    return encantamentos[opcao - 1]


# TELA PARA ADICIONAR O PRODUTO
# Reúne os dados necessários para cadastrar um produto.
def adicionar_produto(inventario=None):
    print('━' * 60)
    print('▣ MINESHOP - ADICIONAR PRODUTO')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)

    if inventario is None:
        codigo = validar_itens('▷ ID do produto: ', True)
        if codigo is None:
            return None
    else:
        codigo = validar_id('▷ ID do produto: ', inventario)
        if codigo is None:
            return None

    nome = validar_nome('▷ Nome do produto: ', True)
    if nome is None:
        return None
    quantidade = validar_itens('▷ Quantidade: ', True)
    if quantidade is None:
        return None
    preco = validar_decimal('▷ Preço: ', True)
    if preco is None:
        return None
    encantado = validar_compra('▷ Produto encantado? (Sim/Não): ', True)
    if encantado is None:
        return None
    encantamento = ''
    if encantado:
        encantamento = escolher_encantamento()
        if encantamento is None:
            return None

    print('━' * 60)
    print('▷ Dados do produto preenchidos.')
    return [codigo, nome, quantidade, preco, encantado, encantamento]


# TELA PARA REMOVER O PRODUTO
# Solicita os dados para remover um produto do estoque.
def remover_produto(inventario=None):
    print('━' * 60)
    print('▣ MINESHOP - REMOVER PRODUTO')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)

    if inventario is None:
        codigo = validar_itens('▷ ID do produto que deseja remover: ', True)
        if codigo is None:
            return None
    else:
        codigo = validar_id_existente('▷ ID do produto que deseja remover: ', inventario)
        if codigo is None:
            return None

    confirmar = validar_compra('▷ Confirmar remoção? (Sim/Não): ', True)
    if confirmar is None:
        return None

    print('━' * 60)
    if confirmar:
        print('▷ Remoção confirmada.')
        return codigo
    else:
        print('▷ Remoção cancelada.')
        return


# TELA PARA ATUALIZAR O PRODUTO
# Apresenta as opções de edição e valida os novos dados.
def atualizar_produto(inventario=None):
    print('━' * 60)
    print('▣ MINESHOP - ATUALIZAR PRODUTO')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)

    if inventario is None:
        codigo = validar_itens('▷ ID do produto que deseja atualizar: ', True)
        if codigo is None:
            return None
    else:
        codigo = validar_id_existente('▷ ID do produto que deseja atualizar: ', inventario)
        if codigo is None:
            return None

    print('▷ Nome (1)')
    print('▷ Quantidade (2)')
    print('▷ Preço (3)')
    print('▷ Encantado / encantamento (4)')

    campo = validar_itens('▷ O que deseja atualizar? ', True)
    if campo is None:
        return None
    while campo < 1 or campo > 4:
        print('⚠ Erro: Escolha uma opção de 1 a 4.')
        campo = validar_itens('▷ O que deseja atualizar? ', True)
        if campo is None:
            return None

    if campo == 1:
        novo_valor = validar_nome('▷ Novo nome: ', True)
        if novo_valor is None:
            return None
    elif campo == 2:
        novo_valor = validar_itens('▷ Nova quantidade: ', True)
        if novo_valor is None:
            return None
    elif campo == 3:
        novo_valor = validar_decimal('▷ Novo preço: ', True)
        if novo_valor is None:
            return None
    else:
        novo_valor = validar_compra('▷ Produto encantado? (Sim/Não): ', True)
        if novo_valor is None:
            return None
        encantamento = ''
        if novo_valor:
            encantamento = escolher_encantamento()
            if encantamento is None:
                return None
        return [codigo, campo, novo_valor, encantamento]

    print('━' * 60)
    print('▷ Dados da atualização preenchidos.')
    return [codigo, campo, novo_valor]


# TELA PARA BUSCAR O PRODUTO
# Coleta o tipo de busca e o valor que será pesquisado.
def buscar_produto():
    print('━' * 60)
    print('▣ MINESHOP - BUSCAR PRODUTO')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)
    print('▷ Buscar por ID (1)')
    print('▷ Buscar por nome exato (2)')
    print('▷ Buscar por parte do nome (3)')

    tipo = validar_itens('▷ Escolha uma opção: ', True)
    if tipo is None:
        return None
    while tipo < 1 or tipo > 3:
        print('⚠ Erro: Escolha 1, 2 ou 3.')
        tipo = validar_itens('▷ Escolha uma opção: ', True)
        if tipo is None:
            return None

    if tipo == 1:
        valor = validar_itens('▷ ID do produto: ', True)
        if valor is None:
            return None
    else:
        valor = validar_nome('▷ Nome do produto: ', True)
        if valor is None:
            return None

    print('━' * 60)
    print('▷ Dados da busca preenchidos.')
    return [tipo, valor]


# TELA PARA MOSTRAR OS PRODUTOS
# Exibe o cabeçalho da consulta de produtos.
def mostrar_produtos():
    print('━' * 60)
    print('▣ MINESHOP - MOSTRAR PRODUTOS')
    print('━' * 60)
    print('▷ Lista de produtos cadastrados.')
    print('━' * 60)

# TELA PARA ESTATÍSTICAS
# Identifica a tela de estatísticas do estoque.
def mostrar_estatisticas():
    print('━' * 60)
    print('▣ MINESHOP - ESTATÍSTICAS')
    print('━' * 60)
    print('▷ Quantidade de produtos e valor total do inventário.')
    print('━' * 60)

# TELA PARA ALTERAR LOGIN
# Apresenta a opção de alteração das credenciais.
def tela_alterar_login():
    print('━' * 60)
    print('▣ MINESHOP - ALTERAR LOGIN')
    print('━' * 60)
    print('▷ Alteração de usuário e senha.')
    print('━' * 60)

# TELA PARA SALVAR E SAIR
# Solicita os dados do item coletado pelo jogador.
def tela_coletar():
    print('━' * 60)
    print('▣ MINESHOP - COLETAR ITEM')
    print('▷ Digite V para voltar sem concluir a operação.')
    print('━' * 60)
    nome = validar_nome('▷ Nome do novo item: ', True)
    if nome is None:
        return None
    while ';' in nome:
        print('⚠ Erro: O nome não pode conter ponto e vírgula.')
        nome = validar_nome('▷ Nome do novo item: ', True)
        if nome is None:
            return None
    quantidade = validar_itens('▷ Quantidade: ', True)
    if quantidade is None:
        return None
    while quantidade == 0:
        print('⚠ Erro: Informe uma quantidade maior que zero.')
        quantidade = validar_itens('▷ Quantidade: ', True)
        if quantidade is None:
            return None
    encantado = validar_compra('▷ Item encantado? (Sim/Não): ', True)
    if encantado is None:
        return None
    encantamento = ''
    if encantado:
        encantamento = escolher_encantamento()
        if encantamento is None:
            return None
    return [nome, quantidade, encantado, encantamento]


# Solicita o item e a quantidade que serão retirados do inventário pessoal.
def tela_remover_item():
    print('━' * 60)
    print('▣ MINESHOP - REMOVER ITEM DO INVENTÁRIO')
    print('▷ Digite V para voltar sem concluir a operação.')
    codigo = validar_itens('▷ ID do seu item: ', True)
    if codigo is None:
        return None
    quantidade = validar_itens('▷ Quantidade para remover: ', True)
    if quantidade is None:
        return None
    confirmar = validar_compra('▷ Confirmar descarte? (Sim/Não): ', True)
    if confirmar:
        return codigo, quantidade
    return None


# Coleta a quantidade que o jogador deseja disponibilizar para venda.
def tela_disponibilidade():
    print('▣ MINESHOP - QUANTIDADE DISPONÍVEL PARA VENDA')
    print('▷ Digite V para voltar. Zero reserva todas as unidades.')
    codigo = validar_itens('▷ ID do seu item: ', True)
    if codigo is None:
        return None
    quantidade = validar_itens('▷ Quantidade disponível para venda: ', True)
    if quantidade is None:
        return None
    return codigo, quantidade
