#ord = Recebe um único caractere(str de tamnho1) e devovlve o número inteiro correpondente
#       a ele na tabela Unicode (que engloba o ASCII).

#chr = Faz o caminho inverso de ord(): recebe um número inteiro e devolve a string de 1
#       caractere correspondente na tabela Unicode.

#islower() = Retorna True se houver pelo menos um caractere alfabético na string e todos 
#           os caracteres alfabéticos forem minúsculos (False se não houver letras,
#            como "123 " ou "").

#isupper() = Retorna True se houver pelo menos um caractere alfabético na string e todos 
#           os caracteres alfabéticos forem maiúsculos.

#--------------------------------------------------------------------------------

# for caractere in texto: -> VERIFICA SE A LETRA É MINÚSCULA, MAIÚSCULA OU OUTRO CARACTERE
#   if caractere.islower():
#     print(caractere, "-> minúscula")
#   elif caractere.isupper():
#     print(caractere, "-> maiúscula")
#   else:
#     print(caractere, "-> outro caractere")

#---------------------------------------------------------------------------------

# for caractere in texto: -> VAI FAZER O "a" SER A POSIÇÃO 0, ONDE "z" VIRA 25
#   if caractere.islower():
#     pos = ord(caractere) - ord("a")
#     print(caractere, "-> posição 0..25:", pos)
#   else:
#     print(caractere, "-> ignorado neste teste")


# for caractere in texto: -> TRÁS A POSIÇÃO NOVA DO CARACTERE SUBTRAINDO PELA PRÓPRIA POSIÇÃO ANTIGA
#   if caractere.islower():
#     pos = ord(caractere) - ord("a")
#     nova_pos = (pos + chave) % 26
#     print(caractere, "-> nova pos:", nova_pos)

# for caractere in texto: -> AQUI ELE FAZ A SUBSTITUIÇÃO ONDE O ELEMENTO ESCRITO É SUBSTITUÍDO PELO OUTRO DAS CASAS A FRENTE
#   if caractere.islower():
#     pos = ord(caractere) - ord("a")
#     nova_pos = (pos + chave) % 26
#     letra_cifrada = chr(ord("a") + nova_pos)
#     print(caractere, "->", letra_cifrada)

# resultado = ""

# for caractere in texto:
#   if caractere.islower():
#     pos = ord(caractere) - ord("a")
#     nova_pos = (pos + chave) % 26
#     resultado += chr(ord("a") + nova_pos)
#   elif caractere.isupper():
#     pos = ord(caractere) - ord("A")
#     nova_pos = (pos + chave) % 26
#     resultado += chr(ord("A") + nova_pos)
#   else:
#     resultado += caractere

# print("Texto cifrado:", resultado)

chave_cesar = 7

def cifrar_cesar(campo, chave):
    campo = str(campo)
    resultado = ""

    minusculas = "abcdefghijklmnopqrstuvwxyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digitos = "0123456789"
    acentos_min = "áàâãéêíóôõúç"
    acentos_mai = "ÁÀÂÃÉÊÍÓÔÕÚÇ"

    for caractere in campo:
        if caractere in minusculas:
            resultado += auxiliar(caractere, minusculas , chave)
        elif caractere in maiusculas:
            resultado += auxiliar(caractere, maiusculas, chave)
        elif caractere in digitos:
            resultado += auxiliar(caractere, digitos, chave)
        elif caractere in acentos_min:
            resultado += auxiliar(caractere, acentos_min, chave)
        elif caractere in acentos_mai:
            resultado += auxiliar(caractere, acentos_mai, chave)
        else:
            resultado += caractere
    return resultado

def auxiliar(caractere, grupo, chave):
    idx = grupo.index(caractere)
    novo_idx = (idx + chave) % len(grupo)
    return grupo[novo_idx]

# cifrado = cifrar_cesar(texto, 10)
# decifrar = cifrar_cesar(cifrado, -10)
# print("Cifrado:", cifrado)
# print("Decifrado:", decifrar)
