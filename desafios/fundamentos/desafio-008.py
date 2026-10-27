print('8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.\n')
num = float(input('Digite um valor em metros: '))
print('O valor digitado em centímetros é {:.0f}cm \nO valor digitado em milímetros é {:.0f}mm'.format((num * 100), (num * 1000)))