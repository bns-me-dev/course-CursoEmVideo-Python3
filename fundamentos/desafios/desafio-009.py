print('===== DESAFIO 09 =====')
num = int(input('Digite um número inteiro: '))
print('A tabuada de {} é:'.format(num))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, (num * i)))