"""
A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com
a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER
"""

from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento do atleta: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'IDADE DO ATLETA: {idade} anos\nCATEGORIA DO ATLETA: ', end='')

# Uma observação:
# Se eu construo condições faixa de valores nesse modelo mas inverto a
# ordem, começando pelo maior, se eu digito um valor menor, que era
# para entrar numa faixa inferior, a condição assume que é a maior,
# porque se eu digito 9, e as condições são nessa sequência: 9 <= 14
# e 9 <= 9, ambas relacionadas numa mesma estrutura condicional, a
# segundo condição, que seria o que normalmente eu quero, nunca será
# executada. 
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
