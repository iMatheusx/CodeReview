# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço
# do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipo = input('Escolha se deseja álcool ou gasolina (A / G): ')
litr = float(input('Quants litros você deseja? '))

desc_alcool1 = 1.9 * 0.03
desc_alcool2 = 1.9 * 0.05
desc_gas1 = 2.5 * 0.04
desc_gas2 = 2.5 * 0.06

if tipo == 'A' or tipo == 'a':
    if litr <= 20:
        print(f'o valor com o desconto será de {(1.9 - desc_alcool1) * litr}')
    elif litr > 20:
        print(f'o valor com o desconto será de {(1.9 - desc_alcool2) * litr}')
elif tipo == 'G' or tipo == 'g':
    if litr <= 20:
        print(f'o valor com o desconto será de {(2.5 - desc_gas1) * litr}')
    elif litr > 20:
        print(f'o valor com o desconto será de {(2.5 - desc_gas2) * litr}')