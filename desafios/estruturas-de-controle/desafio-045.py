from random import randint

print('45 - Crie um programa que faça o computador jogar Jokenpô com você.\n')

num = int(input('Vamos jogar Jokenpô! Escolha um número:\n 0 para Pedra\n 1 para Papel\n 2 para Tesoura\nDigite aqui: '))
num_comp = randint(0, 2)

if num_comp == 0:
    print(' O computador escolheu Pedra!')
elif num_comp == 1:
    print(' O computador escolheu Papel!')
elif num_comp == 2:
    print(' O computador escolheu Tesoura!')

if num == num_comp:
    print('Empate!')
elif (num == 0 and num_comp == 2) or (num == 1 and num_comp == 0) or (num == 2 and num_comp == 1):
    print(' Você venceu!')
else:
    if num > 2:
        print(' Você informou um número inválido!')
    else:
        print(' O computador venceu!')
