print('===== DESAFIO 31 =====')
num = int(input('Informe a distância do seu destino em Km: '))

if num <= 200:
    print(f' O valor da sua passagem será: R$ {num * 0.50:.2f}')
else:
    print(f' O valor da sua passagem será: R$ {num * 0.45:.2f}')