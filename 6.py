# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                     Até 5 Kg           Acima de 5 Kg

# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg

# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_maçã = float(input('Quants kgs maçã você deseja? (se não quiser maçã digite o valor igual a 0): '))
kg_morango= float(input('Quants kgs de morango você deseja? (se não quiser morango digite o valor igual a 0): '))
desc_morango1 = 2.5 * kg_morango
desc_morango2 = 2.2 * kg_morango
desc_morango3 = desc_morango2 * 0.10
desc_maça1 = 1.8 * kg_maçã
desc_maça2 = 1.5 * kg_maçã
desc_maça3 = desc_maça2 * 0.10
valor_MaçaMorango = desc_morango2 + desc_maça2

if kg_maçã == 0:
    if kg_morango <= 5:
        print(f'O total da compra de {kg_morango}kg morangos será de: R${desc_morango1} ')
    elif kg_morango > 5 and kg_morango <= 8:
        print(f'O total com o desconto pela compra de {kg_morango}kg de morangos será de: R${desc_morango2}')
    elif kg_morango > 8:
        print(f'O total com o desconto pela compra de {kg_morango}kg de morangos será de: R${desc_morango2 - desc_morango3}')
elif kg_morango == 0:
    if kg_maçã <= 5:
        print(f'O total da compra de {kg_maçã}kg maçã será de: R${desc_maça1} ')
    elif kg_maçã > 5 and kg_maçã <= 8:
        print(f'O total com o desconto pela compra de {kg_maçã}kg de maçã será de: R${desc_maça2}')
    elif kg_maçã > 8:
        print(f'O total com o desconto pela compra de {kg_maçã}kg de maçã será de: R${desc_maça2 - desc_maça3}')
elif valor_MaçaMorango > 25:
    if kg_morango > 5 and kg_maçã > 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça2 + desc_morango2) * 0.9}')
    elif kg_morango > 5 and kg_maçã <= 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça1 + desc_morango2) * 0.9}')
    elif kg_morango <= 5 and kg_maçã > 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça2 + desc_morango1) * 0.9}')
elif kg_morango + kg_maçã > 8:
    if kg_morango <= 5 and kg_maçã <= 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça1 + desc_morango1) * 0.9}')
    elif kg_morango > 5 and kg_maçã <= 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça1 + desc_morango2) * 0.9}')
    elif kg_morango <= 5 and kg_maçã > 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça2 + desc_morango1) * 0.9}')
    elif kg_morango > 5 and kg_maçã > 5:
        print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${(desc_maça2 + desc_morango2) * 0.9}')
elif kg_morango <=5 and kg_maçã <=5:
    print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${desc_maça1 + desc_morango1}')
elif kg_morango > 5 and kg_maçã <=5:
    print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${desc_maça1 + desc_morango2}')
elif kg_morango <=5 and kg_maçã > 5:
    print(f'O total da compra de {kg_morango}kg de morango e {kg_maçã}kg de maçã será de: R${desc_maça2 + desc_morango1}')

