# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

p1 = input("Telefonou para a vítima? (SIM / NÃO): ")
p2 = input("Esteve no local do crime? (SIM / NÃO): ")
p3 = input("Mora perto da vítima? (SIM / NÃO): ")
p4 = input("Devia para a vítima? (SIM / NÃO): ")
p5 = input("Já trabalhou com a vítima? (SIM / NÃO): ")
n = 0
if p1 == "SIM" or p1 == "sim" or p1 == "Sim":
    n = n + 1
if p2 == "Sim" or p2 == "SIM" or p2 == "sim":
    n = n + 1
if p3 == "Sim" or p3 == "SIM" or p3 == "sim":
    n = n + 1
if p4 == "Sim" or p4 == "SIM" or p4 == "sim":
    n = n + 1
if p5 == "Sim" or p5 == "SIM" or p5 == "sim":
    n = n + 1
if n == 2:
    print('Essa pessoa pode ser considerada um suspeito no caso')
elif n == 3 or n == 4:
    print('Essa pessoa pode ser considerada como cúmplice no caso')
elif n == 5:
    print('Essa pessoa pode ser considerada como assasino')
print(f'o número de resposta do entrevistado foi {n}')