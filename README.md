# Mineshop

Projeto de Programação II desenvolvido em Python, inspirado nas trocas com aldeões do Minecraft. A proposta é criar um sistema de gerenciamento de inventário pelo terminal.

## Funcionalidades

O Villager administra o catálogo de produtos por login; o Jogador acessa a loja para consultar itens e, após a integração, comprar e trocar usando esmeraldas. O sistema também terá busca, ordenação, estatísticas e armazenamento cifrado do inventário.

**Em desenvolvimento:** os menus dos dois perfis funcionam. O CRUD do inventário, as compras, as trocas, a busca real, a ordenação e o salvamento em CSV cifrado ainda dependem da integração dos módulos do grupo.

## Estrutura

- `main.py` — início do programa e acesso ao menu.
- `interface.py` — telas e validações de entrada.
- `autenticacao.py` — cadastro, login e alteração de credenciais.
- `inventario.py` — reservado para o gerenciamento do inventário.
- `login.py` — arquivo ainda não implementado.

## Como executar

Com o Python 3 instalado, execute na pasta do projeto:

```bash
python main.py
```

No início, escolha Villager (administrador) ou Jogador. No primeiro acesso como Villager, o programa solicita a criação de um login; o Jogador não precisa de login. O único login do arquivo `login.txt` pertence ao Villager.

## Desenvolvimento

O projeto está sendo feito em grupo. A interface e as validações estão em andamento, enquanto as funcionalidades dos demais módulos serão integradas ao longo do desenvolvimento.
