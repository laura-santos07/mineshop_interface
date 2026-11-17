# IMPORTANDO FUNÇÕES DE ARQUIVOS EXTERNOS
from autenticacao import criar_login
from interface import menu, escolher_opcao, validar_compra, adicionar_produto, remover_produto, atualizar_produto, buscar_produto

if criar_login(): # Procura criar_login, executa e aplica a condição
    menu()
    opcao = escolher_opcao()
    print('Opção selecionada:', opcao)

    if opcao == 1:
        adicionar_produto()

    elif opcao == 2:
        remover_produto()

    elif opcao == 3:
        atualizar_produto()

    elif opcao == 4:
        buscar_produto()