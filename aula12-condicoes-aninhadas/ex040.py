"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superios: APROVADO
"""

# Observação para futura melhoria:
# O usuário pode digitar valores acima de 10
# e abaixo de 0.
# Corrigir as entradas, corrige automaticamente
# oa valores correspondentes à média.
nota1 = float(input('Informe a sua 1ª nota: '))
nota2 = float(input('Informe a sua 2ª nota: '))

media = (nota1 + nota2) / 2

print(f'Sua média foi {media:.1f}\nSituação: ', end='')

if media < 5:
    print('REPROVADO')

# Uma forma usando 2 condições e 1 operador lógico
# elif media >= 5 and media < 7:

# Outra forma usando 1 condição com 3 fatores
# e 2 operadores relacionais.

# O Python permite fazer isso e
# se chama sintaxe de comparação em cadeia.
elif 5 <= media < 7:
    print('RECUPERAÇÃO')

else:
    print('APROVADO')
