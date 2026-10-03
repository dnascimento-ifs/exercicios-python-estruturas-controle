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

# ano_atual = date.today().year
ano_atual = int(input('Informe o ano que deseja analisar (0 para ano atual): '))

if ano_atual == 0:
    ano_atual = date.today().year

# Por que essa condição agora existe?
# Porque quando eu dou ao usuário a opção de definir o ano de análise,
# ele pode digitar um ano antes do ano de nascimento do participante,
# deixando o tempo e idade incorretos!
if ano_atual >= ano_nascimento:
    idade = ano_atual - ano_nascimento

    print(f'Em {ano_atual} você tem {idade} anos.')

    # Olhar as saídas para corrigir erro de saída de dados

    if idade == 18:
        print('Está na hora de se alistar!')

    elif idade < 18:
        print(f'Não está na hora de se alistar!\nFaltam {18 - idade} anos.')

    else:
        print(f'Já passou da hora de se alistar!\nVocê deve ter se alistado há {idade - 18} anos.')

else:
    print(f'Não tem como essa pessoa se alistar no ano de {ano_atual}, pois ela nasceu em {ano_nascimento}!')
