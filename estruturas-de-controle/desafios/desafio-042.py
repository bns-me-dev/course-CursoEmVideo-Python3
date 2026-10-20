print('===== DESAFIO 42 =====')
num1 = float(input('Informe o valor da primeira reta: '))
num2 = float(input('Informe o valor da segunda reta: '))
num3 = float(input('Informe o valor da terceira reta: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print(' Os valores informados podem formar um triângulo: ')
    if num1 == num2 == num3:
        print('  #EQUILÁTERO.')
    elif num1 != num2 != num3 != num1:
        print('  #ESCALENO.')
    else:
        print('  #ISÓSCELES.')
else:
    print('Os valores informados não podem formar um triângulo.')
