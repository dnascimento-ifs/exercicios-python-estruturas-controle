"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

print("""Suas Opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")

opcao_user = int(input('Qual a sua jogada? ')) - 1

itens = ['PEDRA', 'PAPEL', 'TESOURA']

from random import randint

opcao_pc = randint(0, 2)

from time import sleep

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 10)
print(f'COMPUTADOR jogou \033[94m{itens[opcao_pc]}\033[0m')
print(f'JOGADOR jogou \033[94m{itens[opcao_user]}\033[0m')
print('-=' * 10)

if (opcao_user == 0 and opcao_pc == 2) or (opcao_user == 1 and opcao_pc == 0) or (opcao_user == 2 and opcao_pc == 1):
    print('JOGADOR \033[92mVENCEU!\033[0m')

elif (opcao_user == 0 and opcao_pc == 0) or (opcao_user == 1 and opcao_pc == 1) or (opcao_user == 2 and opcao_pc == 2):
    print('\033[95mEMPATE!\033[m')

elif (opcao_user == 0 and opcao_pc == 1) or (opcao_user == 1 and opcao_pc == 2) or (opcao_user == 2 and opcao_pc == 0):
    print('JOGADOR \033[91mPERDEU!\033[0m')

print('-=' * 10)
