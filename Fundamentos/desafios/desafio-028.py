from random import randint

print('===== DESAFIO 28 =====')
num = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
user_num = int(input('Em que número eu pensei? '))

print('Parabéns! Você acertou!' if user_num == num else 'Você errou! Eu pensei no número {}.'.format(num))