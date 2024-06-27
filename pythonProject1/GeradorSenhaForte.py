import random
import string


def gerar_cacactere_aleatorio():
    return random.choice(string.ascii_letters)


def gerar_caractere_especial():
    return random.choice(string.punctuation)


def gerar_numero_aleatorio(numero_inicial, numero_final):
    return random.randint(numero_inicial, numero_final)


senhaForte = ""
intervalo_caractere_especial = None
cont = None
for i in range(gerar_numero_aleatorio(8, 20)):
    if i == 0 or cont == intervalo_caractere_especial:
        senhaForte = senhaForte + gerar_caractere_especial()
        intervalo_caractere_especial = gerar_numero_aleatorio(1, 3)
        cont = 1
    else:
        senhaForte = senhaForte + gerar_cacactere_aleatorio()
print(senhaForte)
