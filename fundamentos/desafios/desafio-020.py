from random import shuffle

print('===== DESAFIO 20 =====')
stg1 = input('Digite o nome do aluno 1: ')
stg2 = input('Digite o nome do aluno 2: ')  
stg3 = input('Digite o nome do aluno 3: ')
stg4 = input('Digite o nome do aluno 4: ')
list = [stg1, stg2, stg3, stg4]
shuffle(list)
print('A ordem de apresentação será: {}'.format(list))