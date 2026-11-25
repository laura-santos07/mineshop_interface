# IMPORTANDO FUNÇÕES DE ARQUIVOS EXTERNOS
from autenticacao import criar_login, alterar_login
from interface import menu_inicial, escolher_perfil, menu, escolher_opcao
from interface import adicionar_produto, remover_produto, atualizar_produto, buscar_produto
from interface import mostrar_produtos, mostrar_estatisticas, tela_alterar_login
from interface import menu_jogador, escolher_opcao_jogador, tela_comprar, tela_vender, tela_inventario_jogador
from interface import tela_coletar, tela_remover_item, tela_disponibilidade
import busca_e_ordenacao as busca
import inventario as inv


def consultar_produto(inventario):
    dados = buscar_produto()
    if dados is None:
        return
    resultados = busca.buscar(inventario, dados[0], dados[1])
    if not resultados:
        print('▷ Produto não encontrado.')
        input('Pressione ENTER para voltar ao menu...')
        return
    encontrados = {}
    for registro in resultados:
        encontrados[registro[0]] = registro[1:]
    inv.mostrar_produtos(encontrados)


def executar():
    perfil = 0
    inventario = None
    jogador = None
    esmeraldas = None
    disponibilidade = None

    while perfil != 3:
        menu_inicial()
        perfil = escolher_perfil()

        if perfil == 1:
            # Login único para ambos os perfis
            if criar_login():
                if inventario is None:
                    inventario = inv.carregar_inventario()
                    if inventario is None:
                        return
                opcao = 0

                while opcao != 8:
                    # A opção 0 volta à seleção de perfil sem salvar ainda
                    menu()
                    opcao = escolher_opcao()

                    if opcao == 0:
                        break

                    elif opcao == 1:
                        dados = adicionar_produto(inventario)
                        if dados is None:
                            continue
                        if ';' in dados[1]:
                            print('▷ O nome não pode conter ponto e vírgula.')
                        elif inv.adicionar_produto(inventario, dados):
                            print('▷ Produto cadastrado com sucesso!')
                        else:
                            print('▷ ID ou produto com mesmo nome e encantamento já cadastrado.')

                    elif opcao == 2:
                        if len(inventario) == 0:
                            print('▷ Nenhum produto cadastrado.')
                        else:
                            codigo = remover_produto(inventario)
                            if codigo is not None:
                                if inv.remover_produto(inventario, codigo):
                                    print('▷ Produto removido com sucesso!')

                    elif opcao == 3:
                        if len(inventario) == 0:
                            print('▷ Nenhum produto cadastrado.')
                        else:
                            dados = atualizar_produto(inventario)
                            if dados is None:
                                continue
                            if dados[1] == 1 and ';' in dados[2]:
                                print('▷ O nome não pode conter ponto e vírgula.')
                            elif inv.atualizar_produto(inventario, dados):
                                print('▷ Produto atualizado com sucesso!')
                            else:
                                print('▷ Atualização recusada: produto duplicado ou inválido.')

                    elif opcao == 4:
                        consultar_produto(inventario)

                    elif opcao == 5:
                        mostrar_produtos()
                        inv.mostrar_produtos(inventario)

                    elif opcao == 6:
                        mostrar_estatisticas()
                        inv.mostrar_estatisticas(inventario)

                    elif opcao == 7:
                        tela_alterar_login()
                        confirmar = input('▷ Alterar credenciais? (S/N ou V para voltar): ').lower()
                        if confirmar == 's':
                            if alterar_login():
                                print('▷ Credenciais alteradas com sucesso.')
                            else:
                                print('▷ Alteração não realizada.')

                    elif opcao == 8:
                        perfil = 3

                    if opcao not in [4, 5, 8]:
                        input('Pressione ENTER para voltar ao menu...')

        elif perfil == 2:
            # O jogador não recebe acesso à edição de produtos
            if inventario is None:
                inventario = inv.carregar_inventario()
                if inventario is None:
                    return
            if jogador is None:
                jogador = inv.carregar_inventario("inventario_jogador.csv")
                if jogador is None:
                    return
                esmeraldas = inv.carregar_esmeraldas()
                if esmeraldas is None:
                    return
                disponibilidade = inv.carregar_disponibilidade(jogador)
                if disponibilidade is None:
                    return
            opcao_jogador = 0

            while opcao_jogador != 9:
                inv.atualizar_precos_jogador(inventario, jogador)
                menu_jogador()
                opcao_jogador = escolher_opcao_jogador()

                if opcao_jogador == 1:
                    mostrar_produtos()
                    inv.mostrar_produtos(inventario)

                elif opcao_jogador == 2:
                    print(f'▷ Saldo: {esmeraldas:.2f} esmeraldas')
                    if inv.mostrar_produtos(inventario, True):
                        dados = tela_comprar()
                        if dados is None:
                            continue
                        codigo, quantidade = dados
                        esmeraldas, mensagem = inv.comprar_item(inventario, jogador, esmeraldas, codigo, quantidade, disponibilidade)
                        print(mensagem)
                        print(f'▷ Saldo: {esmeraldas:.2f} esmeraldas')
                    else:
                        continue

                elif opcao_jogador == 3:
                    print('▷ Seus itens (use o ID do seu inventário):')
                    if inv.mostrar_itens_venda(inventario, jogador, disponibilidade):
                        dados = tela_vender()
                        if dados is None:
                            continue
                        codigo, quantidade = dados
                        esmeraldas, mensagem = inv.vender_item(inventario, jogador, esmeraldas, codigo, quantidade, disponibilidade)
                        print(mensagem)
                        print(f'▷ Saldo: {esmeraldas:.2f} esmeraldas')
                    else:
                        continue

                elif opcao_jogador == 4:
                    tela_inventario_jogador()
                    print(f'▷ Saldo: {esmeraldas:.2f} esmeraldas')
                    inv.mostrar_produtos(jogador, disponibilidade=disponibilidade)

                elif opcao_jogador == 5:
                    dados = tela_coletar()
                    if dados is None:
                        continue
                    print(inv.coletar_item(inventario, jogador, dados, disponibilidade))
            
                elif opcao_jogador == 6:
                    if not inv.mostrar_produtos(jogador, True, 'Escolher item para remover'):
                        continue
                    dados = tela_remover_item()
                    if dados is None:
                        continue
                    codigo, quantidade = dados
                    print(inv.remover_item_jogador(jogador, codigo, quantidade, disponibilidade))

                elif opcao_jogador == 7:
                    if not inv.mostrar_produtos(jogador, True, 'Escolher item', disponibilidade):
                        continue
                    dados = tela_disponibilidade()
                    if dados is None:
                        continue
                    print(inv.definir_disponibilidade(jogador, disponibilidade, dados[0], dados[1]))

                elif opcao_jogador == 8:
                    consultar_produto(inventario)

                elif opcao_jogador == 9:
                    break

                if opcao_jogador not in [1, 4, 8, 9]:
                    input('Pressione ENTER para voltar ao menu...')

    # As alterações são gravadas somente ao encerrar o programa
    try:
        if inventario is not None:
            inv.salvar_inventario(inventario)
        if jogador is not None:
            inv.atualizar_precos_jogador(inventario, jogador)
            inv.salvar_inventario(jogador, 'inventario_jogador.csv')
            inv.salvar_esmeraldas(esmeraldas)
            inv.salvar_disponibilidade(disponibilidade)
    except OSError:
        print('▷ Erro ao salvar. Alguns arquivos podem ter sido atualizados.')
        return
    print('▷ Até a próxima visita ao Mineshop!')


executar()
