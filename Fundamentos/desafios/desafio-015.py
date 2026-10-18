print('===== DESAFIO 15 =====')
num = float(input('Por quantos dias você alugou o carro? '))
num1 = float(input('Quantos km você rodou com o carro? '))
print('O total a pagar é R$ {:.2f}'.format((num * 60) + (num1 * 0.15)))