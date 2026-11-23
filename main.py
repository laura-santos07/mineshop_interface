# IMPORTANDO FUNÇÕES DE ARQUIVOS EXTERNOS
from autenticacao import criar_login, alterar_login
from interface import menu_inicial, escolher_perfil, menu, escolher_opcao
from interface import adicionar_produto, remover_produto, atualizar_produto, buscar_produto
from interface import mostrar_produtos, mostrar_estatisticas, tela_alterar_login, tela_sair
from interface import menu_jogador, escolher_opcao_jogador, tela_comprar, tela_trocar, tela_inventario_jogador

perfil = 0

while perfil != 3:
    menu_inicial()
    perfil = escolher_perfil()

    if perfil == 1:
        # O unico login do arquivo login.txt pertence ao Villager.
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

        perfil = 3

    elif perfil == 2:
        # O jogador nao recebe acesso ao cadastro ou a edicao de produtos.
        opcao_jogador = 0

        while opcao_jogador != 6:
            menu_jogador()
            opcao_jogador = escolher_opcao_jogador()

            if opcao_jogador == 1:
                mostrar_produtos()
                print('▷ O catálogo será conectado ao inventário na integração.')

            elif opcao_jogador == 2:
                tela_comprar()

            elif opcao_jogador == 3:
                tela_trocar()

            elif opcao_jogador == 4:
                tela_inventario_jogador()

            elif opcao_jogador == 5:
                buscar_produto()

    elif perfil == 3:
        print('▷ Até a próxima visita ao Mineshop!')
