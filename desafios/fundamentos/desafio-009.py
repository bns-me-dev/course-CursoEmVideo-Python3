print('9 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.\n')
num = int(input('Digite um número inteiro: '))
print('A tabuada de {} é:'.format(num))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, (num * i)))