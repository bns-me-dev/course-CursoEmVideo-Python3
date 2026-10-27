from math import sin, cos, tan, radians

print('18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n')
num = float(input('Digite um ângulo: '))
print('O ângulo de {} tem : \n SENO = {:.2f}\n COSSENO = {:.2f}\n TANGENTE = {:.2f} '.format(num, sin(radians(num)), cos(radians(num)), tan(radians(num)) ))

