#====================================  IMPORTAÇÕES  ====================================
import hashlib # Gerar Hash

#===========================  LOGIN, AUTENTICAÇÃO E SEGURANÇA  ===========================
login = "login.txt"

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
    try:
        with open(login, "r", encoding="utf-8") as arquivo: # Leitura do arquivo login.txt
            linhas = arquivo.read()

        if not linhas: # Se o arquivo estiver vazio, será solicitado usuário e senha.
            print(barra_sup)
            print(f"{lateral} Crie seu login e senha para acessar o sistema.".ljust(largura_caixa + 1) + lateral)
            print(barra_div)
            nome_usuario = str(input(f"{lateral} Crie o nome de usuário ▸ "))
            senha_usuario = str(input(f"{lateral} Crie a senha ▸ "))
            hash_nome, hash_senha = gerar_hash(nome_usuario, senha_usuario)
            print(barra_div)
            print(f"{lateral} Conta criada com sucesso!".ljust(largura_caixa + 1) + lateral)
            print(barra_inf)

            with open(login, "w", encoding="utf-8") as arquivo:
                arquivo.write(f"{hash_nome};{hash_senha}\n")

            return True # Informa que o cadastro foi feito e libera acesso ao menu

        else: # Se o login existir, os dados de acesso serão solicitados e autenticados
            print(barra_sup)
            print(f"{lateral} Entre com o usuário e a senha cadastrados.".ljust(largura_caixa + 1) + lateral)
            print(barra_div)
            nome_usuario = str(input(f"{lateral} Digite seu nome de usuário ▸ "))
            senha_usuario = str(input(f"{lateral} Digite sua senha ▸ "))
            print(barra_inf)
            return autenticar(nome_usuario, senha_usuario) # Retorna o resultado da autenticação para a função que chama criar_login
        
    except FileNotFoundError: # Caso o arquivo não seja encontrado ele será criado
        with open("login.txt", "w", encoding="utf-8") as arquivo:
            pass

        return criar_login()

        
def autenticar(nome, senha): # Verifica se o hash armazenado em login.txt é o mesmo que o atual informado
    NovoHash_nome, NovoHash_senha = gerar_hash(nome, senha)

    with open(login, "r", encoding="utf-8") as arquivo:
        for linha_arq in arquivo:
            if not linha_arq.strip():
                continue
            nome_salvo, senha_salvo = linha_arq.strip().split(";")
            # Remove quebra de linhas e separa o nome e a senha por ponto e vírgula
        
    print(barra_sup)
    if NovoHash_nome == nome_salvo and NovoHash_senha == senha_salvo:
        print(f"{lateral} Acesso autorizado.".ljust(largura_caixa + 1) + lateral)
        print(barra_inf)
        return True
    else:
        print(f"{lateral} Usuário ou senha incorretos. Tente novamente.".ljust(largura_caixa + 1) + lateral)
        print(barra_inf)
        return criar_login()

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
