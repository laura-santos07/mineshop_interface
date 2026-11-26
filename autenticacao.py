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

def solicitar_credencial(mensagem):
    while True:
        valor = input(mensagem)
        if valor.strip().lower() == 'v':
            return None
        if valor.strip():
            return valor
        print('▷ O campo não pode ficar vazio.')


def gravar_login(nome, senha):
    hash_nome, hash_senha = gerar_hash(nome, senha)
    # Só grava depois de preencher e confirmar todos os dados.
    try:
        with open(login, 'w', encoding='utf-8') as arquivo:
            arquivo.write(f'{hash_nome};{hash_senha}\n')
    except OSError as erro:
        print(f'▷ Não foi possível salvar o login: {erro}')
        return False
    return True


def novos_dados():
    print('▷ Digite V para voltar sem alterar as credenciais.')
    nome = solicitar_credencial(f"{lateral} Crie o nome de usuário ▸ ")
    if nome is None:
        return None
    senha = solicitar_credencial(f"{lateral} Crie a senha ▸ ")
    if senha is None:
        return None
    confirmar = input('▷ Confirmar novas credenciais? (S/N): ').strip().lower()
    if confirmar != 's' and confirmar != 'sim':
        return None
    return nome, senha


def criar_login():
    try:
        with open(login, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.read().strip()
    except FileNotFoundError:
        linhas = ''
    except (OSError, ValueError) as erro:
        print(f'▷ Erro ao ler login.txt: {erro}')
        return False
    if linhas == '':
        print('▷ Crie seu login e senha para acessar o sistema.')
        dados = novos_dados()
        if dados is None or not gravar_login(dados[0], dados[1]):
            return False
        print('▷ Conta criada. Agora entre com as novas credenciais.')
    else:
        dados = linhas.split(';')
        if len(dados) != 2 or len(dados[0]) != 64 or len(dados[1]) != 64:
            print('▷ login.txt inválido. Verifique o arquivo antes de continuar.')
            return False
        for valor in dados:
            for caractere in valor:
                if caractere not in '0123456789abcdef':
                    print('▷ login.txt inválido. Verifique o arquivo antes de continuar.')
                    return False
    while True:
        print(barra_sup)
        print('▷ Login do Mineshop (V para voltar)')
        print(barra_div)
        nome_usuario = solicitar_credencial(f"{lateral} Digite seu nome de usuário ▸ ")
        if nome_usuario is None:
            return False
        senha_usuario = solicitar_credencial(f"{lateral} Digite sua senha ▸ ")
        if senha_usuario is None:
            return False
        print(barra_inf)
        try:
            if autenticar(nome_usuario, senha_usuario):
                return True
        except (OSError, ValueError) as erro:
            print(f'▷ Erro ao autenticar: {erro}')
            return False
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


def alterar_login():
    dados = novos_dados()
    if dados is None:
        return False
    return gravar_login(dados[0], dados[1])


def gerar_hash(nome, senha): #gera hashs
    hash_nome = hashlib.sha256(nome.encode("utf-8")).hexdigest()
    hash_senha = hashlib.sha256(senha.encode("utf-8")).hexdigest()
    # L> Converte bytes em letras e números
    return hash_nome, hash_senha
