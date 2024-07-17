    # #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
try:
    valor_1 = int(input("Digite primeiro valor: "))
    valor_2 = int(input("Digite segundo valor: "))
    resultado = valor_1 + valor_2
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: O valor deve ser um inteiro!")
    exit

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
valor = int(input("Digite primeiro valor: "))
denominador = 5
resultado = valor / denominador
print(f"Resultado da divisão por {denominador}: {resultado}")

## 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
valor = int(input("Digite primeiro valor: "))
multiplicador = int(input("Defina o multiplicador: "))
resultado = valor * multiplicador
print(f"Resultado: {resultado}")

## 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
valor_1 = int(input("Digite um número inteiro : "))
valor_2 = int(input("Digite outro número inteiro: "))
resultado = valor_1 / valor_2
print(f"Resultado: {resultado}")

## 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
valor = int(input("Digite um número: "))
calcular_quadrado = valor ** 2
print(f"Resultado: {resultado}")

#### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
valor_1 = float(input("Digite um número decimal : "))
valor_2 = float(input("Digite outro número decimal: "))
resultado = valor_1 + valor_2
print(f"Resultado: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
lista_numeros = []
valor_1 = float(input("Digite um número decimal : "))
valor_2 = float(input("Digite outro número decimal: "))
lista_numeros.append(valor_1)
lista_numeros.append(valor_2)
media = sum(lista_numeros) / len(lista_numeros)
print(f"Media: {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero = int(input("Digite um número: "))
base = int(input("Defina a base: "))
potencia = base ** numero
print(f"Potência: {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (temperatura * 1.8) + 32
print(f"Temperatura em Fahrenheit: {fahrenheit}")

#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Defina o raio: "))
pi = 3.14
area = pi * (raio ** 2)
print(f"A área do circulo: {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input("Digite seu nome: ").upper
print(f"Seu nome em maiúsculas: {nome}")
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome: ").lower
print(f"Seu nome em minúsculas: {nome}")
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ").strip()
print(frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ").split("/")
dia = data[0]
mes = data[1]
ano = data[2]
print(f"Data: [{dia}/{mes}/{ano}]")  

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(f"{nome}{sobrenome}")

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao_1 = True
expressao_2 = False
resultado = expressao_1 and expressao_2
print(f"Expressão 1: {expressao_1}")
print(f"Expressão 2: {expressao_2}")
print(f"AND: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao_1 = True
expressao_2 = False
resultado = expressao_1 or expressao_2
print(f"Expressão 1: {expressao_1}")
print(f"Expressão 2: {expressao_2}")
print(f"OR: {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao = True
print(f"Expressão: {expressao}")
invertido = not expressao
print(f"Invertido: {invertido}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
valor_1 = int(input("Digite um número: "))
valor_2 = int(input("Digite outro número: "))
if valor_1 == valor_2:
    print(f"{valor_1} == {valor_2}")
else:
    print(f"{valor_1} != {valor_2}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
valor_1 = int(input("Digite um número: "))
valor_2 = int(input("Digite outro número: "))
if valor_1 != valor_2:
    print(f"{valor_1} != {valor_2}")
else:
    print(f"{valor_1} == {valor_2}")

# #### try-except e if

# 21: Conversor de Temperatura
temperatura = float(input("Defina a temperatura: "))
try:
    print(f"Temperatura em Celsius: {(temperatura - 32) / 1.8}")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
# 22: Verificador de Palíndromo
palavra = input("Defina uma palavra: ")
try:
    if palavra == palavra[::-1]:
        print("E palíndromo")
    else:
        print("Não e palíndromo")
except TypeError:
    print("Erro: A palavra deve ser uma string!")

# 23: Calculadora Simples
valor_1 = float(input("Defina o primeiro valor: "))
valor_2 = float(input("Defina o segundo valor: "))
operacao = input("Defina a operação (+, -, *, /): ")
try:
    if operacao == "+":
        print(f"Resultado: {valor_1 + valor_2}")
    elif operacao == "-":
        print(f"Resultado: {valor_1 - valor_2}")
    elif operacao == "*":
        print(f"Resultado: {valor_1 * valor_2}")
    elif operacao == "/":
        print(f"Resultado: {valor_1 / valor_2}")
    else:
        print("Operação inválida!")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")

# 24: Classificador de Números
valor = float(input("Defina um número: "))
if valor > 0:
    print("Positivo")
elif valor < 0:
    print("Negativo")
else:
    print("Nulo")

# 25: Conversão de Tipo com Validação
valor = input("Defina um número: ")
try:
    valor = int(valor)
    print(f"Inteiro: {valor}")
except ValueError:
    print(f"Float: {float(valor)}") 