print('===== DESAFIO 34 =====')
num = float(input('Informe o salário: R$ '))
if num <= 1250:
    print(f' O salário com aumento de 15% será: R$ {num * 1.15:.2f}')
else:
    print(f' O salário com aumento de 10% será: R$ {num * 1.10:.2f}')