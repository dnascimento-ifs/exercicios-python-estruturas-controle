"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista em dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros
"""

preco_produto = float(input('Informe o preço do produto: R$ '))
if preco_produto > 0:
    print(f"""{'-' * 52}
Selecione a opção de pagamento:
{'-' * 52}
[ 1 ] - À vista no dinheiro/cheque (10% de desconto)
[ 2 ] - À vista no cartão (5% de desconto)
[ 3 ] - Em até 2x no cartão (preço normal)
[ 4 ] - Em 3x ou mais no cartão (20% de juros)
{'-' * 52}
""", end='')

    opcao_user = int(input('Sua Opção: '))
    print('-' * 52)

    if opcao_user > 0 and opcao_user <= 4:

        flag = 1

        if opcao_user == 1:
            preco_pagar = preco_produto - (preco_produto * 0.1)

        elif opcao_user == 2:
            preco_pagar = preco_produto - (preco_produto * 0.05)

        elif opcao_user == 3:
            preco_pagar = preco_produto
            quant_parcelas = int(input('Informe a quantidade de parcelas: '))
                    
            if quant_parcelas > 2:
                print('\033[91mERRO!\033[0m A opção de pagamento 3 precisa ter uma quantidade de parcelas a baixo de 2!')

                flag = 0

            elif quant_parcelas <= 0:
                print('\033[91mERRO!\033[0m Informe uma quantidade válida de parcelas!')
                
                flag = 0

        elif opcao_user == 4:
            preco_pagar = preco_produto + (preco_produto * 0.2)
            quant_parcelas = int(input('Informe a quantidade de parcelas: '))
            
            if quant_parcelas <= 2 and quant_parcelas > 0:
                print('\033[91mERRO!\033[0m A opção de pagamento 4 precisa ter uma quantidade de parcelas a cima de 2!')

                flag = 0

            elif quant_parcelas <= 0:
                print('\033[91mERRO!\033[0m Informe uma quantidade válida de parcelas!')

                flag = 0

        if flag == 1:
            print(f'Preço Final: R$ {preco_pagar:.2f}')

            if (opcao_user == 3 or (opcao_user == 4 and quant_parcelas > 2)) and quant_parcelas > 0:
                print(f'Quantidade de Parcelas: {quant_parcelas}')
                print(f'Valor da Parcela: R$ {(preco_pagar / quant_parcelas):.2f}')

    else:
        print('\033[91mERRO!\033[0m Opção inválida, selecione uma oção de pagamento válido!')

else:
    print('\033[91mERRO!\033[0m Valor do produto inválido!')
