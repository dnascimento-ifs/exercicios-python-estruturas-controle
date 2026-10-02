"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço
militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do
prazo.
"""

from datetime import date

ano_nascimento = int(input('Informe seu ano de nascimento: '))

ano_atual = int(input('Informe o ano que deseja analisar (0 para ano atual): '))

if ano_atual == 0:
    ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print(f'Em {ano_atual} você tem {abs(idade)} anos.')

if idade == 18:
    print('Está na hora de se alistar!')

elif idade < 18:
    print(f'Não está na hora de se alistar!\nFaltam {18 - idade} anos.')

else:
    print(f'Já passou da hora de se alistar!\nVocê deveria ter se alistado há {idade - 18} anos.')

