from math import hypot

print('===== DESAFIO 17 =====')
num1 = float(input('Informe o comprimento do cateto oposto: '))
num2 = float(input('Informe o comprimento do cateto adjacente: '))
print('A hipotenusa é: {:.2f}'.format(hypot(num1, num2)))