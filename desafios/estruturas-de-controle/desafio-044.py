print('44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:\n    – à vista dinheiro/cheque: 10% de desconto\n    – à vista no cartão: 5% de desconto\n    – em até 2x no cartão: preço formal\n    – 3x ou mais no cartão: 20% de juros\n')
num1 = float(input('Informe o preço do produto: R$ '))
print('Formas de pagamento:\n 1 - À vista (dinheiro/cheque) \n 2 - À vista (cartão) \n 3 - 2x no cartão \n 4 - 3x ou mais no cartão')
num2 = int(input('Escolha a forma de pagamento: '))

if num2 == 1:
    print('     O preço final é: R$ {:.2f} \n     Houve 10% de desconto.'.format(num1 * 0.9))
elif num2 == 2:
    print('     O preço final é: R$ {:.2f} \n     Houve 5% de desconto.'.format(num1 * 0.95))
elif num2 == 3:
    print('     O preço final é: R$ {:.2f} \n     Não houve desconto.'.format(num1))
elif num2 == 4:
    num3 = int(input('     Informe o número de parcelas: '))
    if num3 >= 3:
        print('     O preço final é: R$ {:.2f} \n     Houve 20% de juros.'.format(num1 * 1.2))
    else:
        print('     O preço final é: R$ {:.2f} \n     Não houve desconto.'.format(num1))    
else:
    print('Opção inválida.')