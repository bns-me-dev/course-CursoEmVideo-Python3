from math import hypot

print('17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.\n')
num1 = float(input('Informe o comprimento do cateto oposto: '))
num2 = float(input('Informe o comprimento do cateto adjacente: '))
print('A hipotenusa é: {:.2f}'.format(hypot(num1, num2)))