# Mineshop

Simulação de negociações do Minecraft para o Projeto de Programação em Python.

## Como executar

Abra o terminal na pasta que contém main.py e os arquivos CSV/TXT.

```bash
python3 main.py
```

No Windows, use `python main.py` ou `py main.py`.
Não é necessário instalar bibliotecas externas. O módulo de autenticação mantém
hashlib e os, que já estavam no código original do grupo.

## Arquivos

- main.py: menu principal e integração dos módulos.
- interface.py: menus e validação dos dados digitados.
- inventario.py: CRUD, compra, venda, coleta, descarte e leitura/gravação.
- busca_e_ordenacao.py: busca por ID, busca linear e binária, Selection Sort e Merge Sort.
- autenticacao.py: cadastro, login e alteração de credenciais.
- inventario.csv: estoque do Villager.
- inventario_jogador.csv: inventário pessoal.
- esmeraldas.txt: saldo do jogador.
- disponibilidade_jogador.csv: ID e quantidade disponível para venda.
- login.txt: hashes das credenciais originais.

## Jogador

1. Ver produtos da loja
2. Comprar item com esmeraldas
3. Vender item por esmeraldas
4. Meu inventário
5. Coletar item para meu inventário
6. Remover item do meu inventário
7. Definir quantidade disponível para venda
8. Buscar produto
9. Voltar ao início

A coleta é livre. Somente itens com oferta correspondente no Villager podem ser
vendidos, pelo preço vigente da loja. A venda aumenta o estoque do Villager.
O descarte não gera esmeraldas. A opção 7 não altera a quantidade total.

## Paginação

N: próxima; P: anterior; I: primeira; F: última; G: escolher página; V: voltar.
O alterna a ordem alfabética nas listagens gerais. C permite escolher um item
nas telas que oferecem essa opção.

## Armazenamento

Cada produto é armazenado em um dicionário cuja chave é o ID inteiro e cujo
valor é uma lista: [nome, quantidade, preço, encantado, encantamento].
O CSV tem seis campos separados por ponto e vírgula, sem cabeçalho.
Os inventários, o saldo e a disponibilidade são gravados apenas no encerramento
normal do programa. A alteração de login é gravada no momento da confirmação.

Se um arquivo de dados estiver ausente ou inválido, o programa informa o erro e
interrompe a sessão sem gravar. Não há criação automática de inventário vazio.
O salvamento usa open, for e write; não cria backups ou arquivos temporários.
Em caso de erro de escrita, alguns arquivos podem ter sido atualizados.
Execute sempre a partir da pasta do projeto.

## Escopo acadêmico

Foram priorizados listas, dicionários, funções, condicionais, repetições,
recursão, busca, ordenação, manipulação de arquivos e try/except. A adaptação
do campo Importado para Encantado e o campo adicional de encantamento devem
ser confirmados com o professor. A autenticação é demonstrativa, não de produção.
Não há criptografia nos CSVs. A coleta livre e os encantamentos sem restrições
por item foram mantidos conforme solicitado.








Mineshop
Projeto de Programação II desenvolvido em Python, inspirado nas trocas com aldeões do Minecraft. A proposta é criar um sistema de gerenciamento de inventário pelo terminal.

Funcionalidades
O Villager administra o catálogo de produtos por login; o Jogador acessa a loja para consultar itens e, após a integração, comprar e trocar usando esmeraldas. O sistema também terá busca, ordenação, estatísticas e armazenamento cifrado do inventário.

Em desenvolvimento: os menus dos dois perfis funcionam. O CRUD do inventário, as compras, as trocas, a busca real, a ordenação e o salvamento em CSV cifrado ainda dependem da integração dos módulos do grupo.

Estrutura
main.py — início do programa e acesso ao menu.
interface.py — telas e validações de entrada.
autenticacao.py — cadastro, login e alteração de credenciais.
inventario.csv — arquivo de dados do inventário, inicialmente vazio; a leitura e a gravação cifrada ainda serão integradas.
busca_e_ordenação.py — algoritmos de busca e ordenação, ainda pendentes de integração ao programa.
Como executar
Com o Python 3 instalado, execute na pasta do projeto:

python main.py
No início, escolha Villager (administrador) ou Jogador. No primeiro acesso como Villager, o programa solicita a criação de um login; o Jogador não precisa de login. O único login do arquivo login.txt pertence ao Villager.

Desenvolvimento
O projeto está sendo feito em grupo. A interface e as validações estão em andamento, enquanto as funcionalidades dos demais módulos serão integradas ao longo do desenvolvimento.