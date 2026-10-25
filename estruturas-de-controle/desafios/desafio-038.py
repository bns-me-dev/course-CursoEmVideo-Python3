print('38 -  Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:\n    – O primeiro valor é maior\n    – O segundo valor é maior\n    – Não existe valor maior, os dois são iguais\n')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')