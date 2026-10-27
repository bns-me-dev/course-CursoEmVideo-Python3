print('33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.\n')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 == num2 == num3:
    print('\nRESULTADO\n Todos os números digitados são iguais.')
else:
    print(f'\nRESULTADO\n O maior número digitado foi: {max(num1, num2, num3)}\n O menor número digitado foi: {min(num1, num2, num3)}')