"""
Escreva um programa para aprovar o empréstimo bancário para a compra de
uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos
anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado.
"""

valor_casa = float(input('Informe o valor da casa: R$ '))
salario_comprador = float(input('Informe o salário do comprador: R$ '))
tempo_anos_pagar = int(input('Informe em quanto anos a casa será paga: '))

prestacao_mensal = valor_casa / tempo_anos_pagar

if prestacao_mensal > (valor_casa * 0.3):
    print('EMPRESTIMO NEGADO!')
else:
    print('EMPRESTIMO APROVADO!')
