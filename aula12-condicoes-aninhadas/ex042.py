"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isocéles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

lado1 = int(input('Informe a medida do 1º lado: '))
lado2 = int(input('Informe a medida do 2º lado: '))
lado3 = int(input('Informe a medida do 3º lado: '))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print('É possível formar um triângulo com os 3 lados!\nTipo do Triângulo: ', end='')

    if lado1 == lado2 and lado2 == lado3:
        print('EQUILÁTERO')

    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('ISOCÉLES')

    else:
        print('ESCALENO')

else:
    print('Não é possível formar um triângulo com essas medidas!')
