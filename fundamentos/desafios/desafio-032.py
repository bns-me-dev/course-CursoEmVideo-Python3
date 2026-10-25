from datetime import date

print('32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.\n')
num = int(input('Informe o ano que deseja analisar, ou digite 0 para analisar o ano atual: '))

if num == 0:
    num = date.today().year
    
print('O ano {} é bissexto? {}'.format(num, 'Sim' if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0) else 'Não'))