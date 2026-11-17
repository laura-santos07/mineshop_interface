# Mineshop

O **Mineshop** é um projeto acadêmico desenvolvido em Python, inspirado no sistema de trocas do Minecraft. A ideia é criar um sistema de inventário pelo terminal, com um visual simples e referências ao jogo.

O projeto está sendo desenvolvido em grupo e ainda não está finalizado. Este repositório contém a versão atual da interface e das validações, além de arquivos que serão integrados às outras partes do sistema.

## Objetivo

Criar um programa de gerenciamento de produtos que permita cadastrar, consultar, atualizar e remover itens, utilizando conceitos de programação e segurança da informação estudados em aula.

Na proposta do Mineshop, os produtos e as operações do inventário serão apresentados dentro de um contexto de trocas com aldeões e esmeraldas.

## Funcionalidades previstas

O menu do programa foi preparado com estas opções:

1. Adicionar produto
2. Remover produto
3. Atualizar produto
4. Buscar produto
5. Mostrar produtos
6. Estatísticas do inventário
7. Alterar login
8. Salvar e sair

**Atenção:** nem todas essas opções estão funcionando ainda. No momento, as telas das opções 1 a 4 mostram mensagens iniciais, mas não executam as operações no inventário. As opções 5 a 8 aparecem no menu e ainda precisam ser integradas ao fluxo principal.

## O que já foi desenvolvido

- Menu principal exibido no terminal, com um desenho de aldeão.
- Telas iniciais para adicionar, remover, atualizar e buscar produtos.
- Validação da opção escolhida no menu.
- Validação de números inteiros não negativos.
- Validação de valores decimais não negativos.
- Validação de respostas de confirmação com Sim ou Não.
- Função para impedir nomes vazios.
- Função para verificar se um ID já foi cadastrado.
- Código de criação e autenticação de login com hash SHA-256.

As funções de validação de nome e ID já foram criadas, mas ainda precisam ser utilizadas quando o cadastro de produtos estiver integrado. A autenticação está implementada em um módulo separado.

## Arquivos do projeto

| Arquivo | Descrição |
| --- | --- |
| `main.py` | Inicia o programa, chama a autenticação e direciona as opções já conectadas ao menu. |
| `interface.py` | Contém o menu, as telas e as funções de validação. |
| `autenticacao.py` | Contém a criação do login, a autenticação e a geração de hashes. |
| `inventario.py` | Arquivo reservado para as funções do inventário; ainda está vazio nesta versão. |
| `login.py` | Arquivo reservado; ainda está vazio nesta versão. |

O arquivo `login.txt` é utilizado para armazenar os hashes de autenticação. Ele deve ser mantido apenas no ambiente local e não deve ser compartilhado com dados reais.

## Como executar

É necessário ter o **Python 3** instalado.

1. Baixe ou clone este repositório.
2. Abra a pasta do projeto no VS Code ou em outro editor.
3. Execute o arquivo principal pelo terminal:

```bash
python main.py
```

Na primeira execução, se o arquivo de login não existir ou estiver vazio, o programa solicita a criação de um usuário e uma senha. Depois, exibe o menu principal.

## Próximas etapas

- Integrar as telas às funções reais de cadastro, remoção, atualização e busca.
- Implementar a listagem de produtos e as estatísticas.
- Conectar a opção de alteração de login ao menu.
- Implementar a leitura e gravação do inventário em arquivo CSV com a criptografia exigida no trabalho.
- Concluir as buscas, a ordenação e os testes do programa.
- Revisar as validações durante a integração entre os módulos.

## Sobre o projeto

O Mineshop foi pensado para aplicar, de forma prática, conteúdos vistos em **Programação II**, com uma temática de Minecraft. O foco é utilizar uma lógica compreensível, organizar o código em funções e integrar as contribuições dos integrantes do grupo.

**Status:** em desenvolvimento.
