print('34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.\n')
num = float(input('Informe o salário: R$ '))
if num <= 1250:
    print(f' O salário com aumento de 15% será: R$ {num * 1.15:.2f}')
else:
    print(f' O salário com aumento de 10% será: R$ {num * 1.10:.2f}')