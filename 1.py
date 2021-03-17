#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).


n1 = int(input('Informe um número para saber se é par ou ímpar:  '))
if n1 % 2 == 0 :
    print('O número é par!!! ')
else:
    print('O número ímpar!!! ')