
# 1. Escreva um programa verifique se o valor inserido é um alpha, se for, mostre uma mensagem de erro e reinicie o programa, se não for encerre o programa.
def receber_valor_numerico():
    while True:
        try:
            valor = float(input("Digite um valor numérico: "))
            print(f"Você digitou o valor: {valor}")
            break
        except ValueError:
            print("Erro: Por favor, digite um valor numérico.")
            continue

# 2. Crie um programa que receba um nome e mostre uma mensagem de boas-vindas.
def user_name():
    while True:
        nome = input("Digite seu nome: ")
        if nome.isdigit():
            print(f"Você digitou um número: {nome}, informe um nome.")

        if nome.isspace():
            print(f"Você digitou um caractere especial: {nome}, informe um nome.")

        else:
            print("Seu nome é: {}, seja bem vindo".format(nome).capitalize())
            break
