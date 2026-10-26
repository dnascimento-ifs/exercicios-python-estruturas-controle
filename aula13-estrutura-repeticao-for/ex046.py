"""
Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1
segundo entre eles.
"""

# Importa a biblioteca com o sleep()
from time import sleep

# Contagem regressiva
# O range() tem que ter o segundo parâmetro atribuído como -1,
# se for no 0 a contagem para no 1
for i in range(10, -1, -1):
    print(i)
    # Aguarda 1 segundo
    sleep(1)

# Simboliza o fim da contagem após o 0
print('KABUUM!!!')
