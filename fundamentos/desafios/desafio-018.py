from math import sin, cos, tan, radians

print('===== DESAFIO 18 =====')
num = float(input('Digite um ângulo: '))
print('O ângulo de {} tem : \n SENO = {:.2f}\n COSSENO = {:.2f}\n TANGENTE = {:.2f} '.format(num, sin(radians(num)), cos(radians(num)), tan(radians(num)) ))

