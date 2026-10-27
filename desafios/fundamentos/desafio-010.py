print('10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.\n')
num = float(input('Digite um valor em reais: R$ '))
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(num, (num / 5.20)))