"""
Escreva um programa que leia dois números inteiros e compare-os.
Mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

num1 = int(input('Informe o 1º valor: '))
num2 = int(input('Informe o 2º valor: '))

if num1 > num2:
    print('O primeiro valor é maior')

elif num1 < num2:
    print('O segundo valor é maior')

else:
    print('Não existe valor maior, os dois são iguais')
