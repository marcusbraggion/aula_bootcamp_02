# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
valor_1 = int(input("Digite primeiro valor: "))
valor_2 = int(input("Digite segundo valor: "))
resultado = valor_1 + valor_2
print(f"Resultado: {resultado}")

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
rint(f"Resultado: {resultado}")

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
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação