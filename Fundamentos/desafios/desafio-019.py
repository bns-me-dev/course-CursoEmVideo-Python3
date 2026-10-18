from random import choice

print('===== DESAFIO 19 =====')
stg1 = input('Digite o nome do aluno 1: ')
stg2 = input('Digite o nome do aluno 2: ')  
stg3 = input('Digite o nome do aluno 3: ')
stg4 = input('Digite o nome do aluno 4: ')
print('O aluno sorteado foi: {}'.format(choice([stg1, stg2, stg3, stg4])))