print('===== DESAFIO 23 =====')
num = int(input('Digite um número (0 a 9999): '))
print('O número digitado foi {}\n Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(num, (num // 1) % 10, (num // 10) % 10, (num // 100) % 10, (num // 1000) % 10))