print('12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n')
num = float(input('Digite o preço do produto: R$ '))
print('O preço do produto com 5% de desconto é R$ {:.2f}'.format(num - (num * 0.05)))