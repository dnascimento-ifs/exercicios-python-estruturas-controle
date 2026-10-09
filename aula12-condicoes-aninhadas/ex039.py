"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço
militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do
prazo.
"""

from datetime import date

ano_nascimento = int(input('Informe seu ano de nascimento (0 para ano atual): '))

if ano_nascimento == 0:
    ano_nascimento = date.today().year

ano_atual = int(input('Informe o ano que deseja analisar (0 para ano atual): '))

if ano_atual == 0:
    ano_atual = date.today().year

sexo_user = str(input('Informe seu sexo (M/F): '))

# Por que essa condição agora existe?
# Porque quando eu dou ao usuário a opção de definir o ano de análise,
# ele pode digitar um ano antes do ano de nascimento do participante,
# deixando o tempo e idade incorretos!
if ano_atual >= ano_nascimento:
    idade = ano_atual - ano_nascimento

    print(f'Se você nasceu em {ano_nascimento}, em {ano_atual} você tem {idade} anos.')

    if sexo_user == 'M':
    
        if idade == 18:
            print('Está na hora de se alistar!')

        elif idade < 18:
            anos_falta_alistamento = 18 - idade
            print(f'Não está na hora de se alistar!\nFaltam {anos_falta_alistamento} anos para você se alistar em {ano_atual + anos_falta_alistamento}')

        else:
            anos_passaram_alistamento = idade - 18
            print(f'Já passou da hora de se alistar!\nVocê deve ter se alistado há {anos_passaram_alistamento} anos em {ano_atual - anos_passaram_alistamento}')

    elif sexo_user == 'F':
        print('Você é mulher, portanto não tem alistamento obrigatório!')

    else:
        print('\033[91mERRO!\033[0m Sexo informado inválido!')

else:
    print(f'Não tem como essa pessoa se alistar no ano de {ano_atual}, pois ela nasceu em {ano_nascimento}!')
