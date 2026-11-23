# IMPORTANDO FUNÇÕES DE ARQUIVOS EXTERNOS
from autenticacao import criar_login, alterar_login
from interface import menu, escolher_opcao, adicionar_produto, remover_produto, atualizar_produto, buscar_produto, mostrar_produtos, mostrar_estatisticas, tela_alterar_login, tela_sair

if criar_login():
    opcao = 0

    while opcao != 8:
        menu()
        opcao = escolher_opcao()

        if opcao == 1:
            adicionar_produto()

        elif opcao == 2:
            remover_produto()

        elif opcao == 3:
            atualizar_produto()

        elif opcao == 4:
            buscar_produto()

        elif opcao == 5:
            mostrar_produtos()
            print('▷ A listagem será conectada ao inventário na integração.')

        elif opcao == 6:
            mostrar_estatisticas()
            print('▷ As estatísticas serão conectadas ao inventário na integração.')

        elif opcao == 7:
            tela_alterar_login()
            alterar_login()
            print('▷ Credenciais alteradas com sucesso.')

        elif opcao == 8:
            tela_sair()
