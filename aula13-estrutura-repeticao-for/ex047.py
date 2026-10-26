"""
Crie um programa que mostre na tela todos os números pares que estão no
intervalo entre 1 e 50.
"""

# O range() tem que ser de 1 a 51,
# pois vai de 0 a 50 começando no 1.
for i in range(1, 51):
    # Se o resto da divisão for igual a 0,
    # o valor é par (divisível por 2.) 
    if i % 2 == 0:
        print(i)

print('FIM!')
