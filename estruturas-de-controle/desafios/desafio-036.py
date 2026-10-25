print('36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.\n')
num1 = float(input('Informe o valor da casa: R$ '))
num2 = float(input('Informe o seu salário: R$ '))
num3 = int(input('Informe em quantos anos você pretende pagar: '))

num4 = num2 * 0.3
num5 = num1 / (num3 * 12)

if num5 <= num4:
    print('\n Empréstimo aprovado!')
else:
    print('\n Empréstimo negado!')