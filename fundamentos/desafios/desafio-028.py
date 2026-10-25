from random import randint

print('28 - Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.\n')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = randint(0, 5)
user_num = int(input('Em que número eu pensei? '))

print('Parabéns! Você acertou!' if user_num == num else 'Você errou! Eu pensei no número {}.'.format(num))