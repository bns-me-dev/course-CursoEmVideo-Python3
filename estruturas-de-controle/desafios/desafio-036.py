print('===== DESAFIO 36 =====')
num1 = float(input('Informe o valor da casa: R$ '))
num2 = float(input('Informe o seu salário: R$ '))
num3 = int(input('Informe em quantos anos você pretende pagar: '))

num4 = num2 * 0.3
num5 = num1 / (num3 * 12)

if num5 <= num4:
    print('\n Empréstimo aprovado!')
else:
    print('\n Empréstimo negado!')