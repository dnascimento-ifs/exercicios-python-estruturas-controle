"""
Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.
"""

numero = int(input('Informe um valor numérico qualquer: '))

# Menu de opções para melhor visualização
print("""Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")

opcao_user = int(input('Sua opção: '))

if opcao_user == 1:
    # Decisão para a opção 1
    # Converter o valor digitado para binário.
    print(f'O valor {numero} convertido para binário é {bin(numero)}')

elif opcao_user == 2:
    # Decisão para a opção 2
    # Converter o valor digitado para octal.
    print(f'O valor {numero} convertido para octal é {oct(numero)}')

    # Usei mais um elif para um teste lógico melhor,
    # pois se eu uso else e coloco a decisão da opção 3
    # se o usuário digita qualquer coisa (menos 1 e 2, pois já foram definidos)
    # vai executar a decisão da opção 3 do menu, ao invés de não executar nada
    # se a opção digitada não for 3.

elif opcao_user == 3:
    # Decisão para a opção 3
    # Converter o valor digitado para hexadecimal.
    print(f'O valor {numero} convertido para hexadecimal é {hex(numero)}')

else:
    print('OPÇÃO INVÁLIDA!')
