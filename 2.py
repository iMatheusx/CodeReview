#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

n1 = float(input('Informe um numero'))

if n1 // 1 == n1:
    print('Esse número é inteiro!!')
else:
    print('Esse número é decimal!!')