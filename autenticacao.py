#====================================  IMPORTAÇÕES  ====================================
import hashlib # Gerar Hash
import os

#===========================  LOGIN, AUTENTICAÇÃO E SEGURANÇA  ===========================
# Usa sempre o login.txt da mesma pasta do programa, independente do terminal.
login = os.path.join(os.path.dirname(__file__), "login.txt")

#--------Estética--------#
largura_caixa = 60
linha = "━" * largura_caixa
sup_esquerdo = "┏"
inf_esquerdo = "┗"
sup_direito = "┓"
inf_direito = "┛"

barra_sup = sup_esquerdo + linha + sup_direito
barra_inf = inf_esquerdo + linha + inf_direito
barra_div = "┣" + linha + "┫"
lateral   = "┃"

def criar_login():
    # Cadastro inicial: executado apenas se o arquivo nao existir ou estiver vazio.
    try:
        with open(login, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.read().strip()
    except FileNotFoundError:
        linhas = ""

    if linhas == "":
        print(barra_sup)
        print(f"{lateral} Crie seu login e senha para acessar o sistema.".ljust(largura_caixa + 1) + lateral)
        print(barra_div)
        nome_usuario = str(input(f"{lateral} Crie o nome de usuário ▸ "))
        senha_usuario = str(input(f"{lateral} Crie a senha ▸ "))
        hash_nome, hash_senha = gerar_hash(nome_usuario, senha_usuario)

        with open(login, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{hash_nome};{hash_senha}\n")

        print(barra_div)
        print(f"{lateral} Conta criada com sucesso!".ljust(largura_caixa + 1) + lateral)
        print(barra_inf)
        print('▷ Agora entre com o usuário e a senha que acabou de cadastrar.')

    # Mesmo no primeiro acesso, exige login antes de abrir o menu do Villager.
    while True:
        print(barra_sup)
        print(f"{lateral} Login do Villager - Administrador".ljust(largura_caixa + 1) + lateral)
        print(barra_div)
        nome_usuario = str(input(f"{lateral} Digite seu nome de usuário ▸ "))
        senha_usuario = str(input(f"{lateral} Digite sua senha ▸ "))
        print(barra_inf)

        if autenticar(nome_usuario, senha_usuario):
            return True

        print('▷ Usuário ou senha incorretos. Tente novamente.')


def autenticar(nome, senha):
    # Compara os hashes sem alterar o login.txt.
    hash_nome, hash_senha = gerar_hash(nome, senha)
    try:
        with open(login, "r", encoding="utf-8") as arquivo:
            for linha_arq in arquivo:
                linha_arq = linha_arq.strip()
                if linha_arq != "":
                    dados = linha_arq.split(";")
                    if len(dados) == 2:
                        if hash_nome == dados[0] and hash_senha == dados[1]:
                            print(barra_sup)
                            print(f"{lateral} Acesso autorizado.".ljust(largura_caixa + 1) + lateral)
                            print(barra_inf)
                            return True
    except FileNotFoundError:
        return False

    return False


def alterar_login(): # Sobrescreve o arquivo com os novos dados de login
    with open(login, "w", encoding="utf-8") as arquivo:
        print(barra_sup)
        print(f"{lateral} Altere seu login.".ljust(largura_caixa + 1) + lateral)
        print(barra_div)
        nome_usuario = str(input(f"{lateral} Crie o nome de usuário ▸ "))
        senha_usuario = str(input(f"{lateral} Crie a senha ▸ "))
        print(barra_inf)
        hash_nome, hash_senha = gerar_hash(nome_usuario, senha_usuario)
        arquivo.write(f"{hash_nome};{hash_senha}\n")


def gerar_hash(nome, senha): #gera hashs
    hash_nome = hashlib.sha256(nome.encode("utf-8")).hexdigest()
    hash_senha = hashlib.sha256(senha.encode("utf-8")).hexdigest()
    # L> Converte bytes em letras e números
    return hash_nome, hash_senha
