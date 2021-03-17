#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

op = input('Informe se você quer fazer uma operação de soma, subtração, multiplicação ou divisão: (+ | - | x | /): ')
n1 = float(input('Informe um numero'))
n2 = float(input('Informe um numero'))
rA = n1 + n2
rS = n1 - n2
rM = n1 * n2
rD = n1 / n2

if op == "+":
    print(f'a soma de {n1} com {n2} é {rA}')
    if rA % 2 == 0:
        print('O número é par!!! ')
    else:
        print('O número ímpar!!! ')
    if rA < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo')
    if rA == round(rA):
        print('Não é decimal')
    else:
        print('É decimal ')
elif op == "-":
    print(f'a subtração de {n1} com {n2} é {rS}')

    if rS % 2 == 0:
        print('O número é par!!! ')
    else:
        print('O número ímpar!!! ')
    if rS < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo')
    if rS == round(rS):
        print('Não é decimal')
    else:
        print('É decimal ')
elif op == "x":
    print(f'a multiplicação de {n1} com {n2} é {rM}')
    if rM % 2 == 0:
        print('O número é par!!! ')
    else:
        print('O número ímpar!!! ')
    if rM < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo')
    if rM == round(rM):
        print('Não é decimal')
    else:
        print('É decimal ')
elif op == "/":
    print(f'a divisão de {n1} com {n2} é {rD}')

    if rD % 2 == 0:
        print('O número é par!!! ')
    else:
        print('O número ímpar!!! ')
    if rD < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo')
    if rD == round(rD):
        print('Não é decimal')
    else:
        print('É decimal ')


