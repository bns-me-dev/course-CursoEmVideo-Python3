print('5 - Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.\n')
num = float(input('Digite um número: '))
print('O número digitado foi {:.1f} ! \nSeu antecessor é {:.1f} e seu sucessor é {:.1f}'.format(num, (num - 1), (num + 1)))
