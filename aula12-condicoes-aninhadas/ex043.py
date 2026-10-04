"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu statusm de acordo com a tabela abaixo>

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e abaixo de 25: Peso ideal
- Entre 25 e abaixo de 30: Sobrepeso
- Entre 30 e abaixo de 35: Obesidade grau I
- Entre 35 e abaixo de 40: Obesidade grau II
- De 40 para cima: Obesidade grau III
"""

peso = float(input('Informe o quanto pesa (kg): '))
altura = float(input('Informe o quanto mede (m): '))

imc = peso / (altura ** 2)

print(f'Índice de Massa Corporal: {imc:.1f}\nTipo de IMC: ', end='')

if imc < 18.5:
    print('ABAIXO DO PESO')

elif imc >= 18.5 and imc < 25:
    print('PESO NORMAL')

elif imc >= 25 and imc < 30:
    print('SOBREPESO')

elif imc >= 30 and imc < 35:
    print('OBESIDADE GRAU I')

elif imc >= 35 and imc < 40:
    print('OBESIDADE GRAU II')

else:
    print('OBESIDADE GRAU III')
