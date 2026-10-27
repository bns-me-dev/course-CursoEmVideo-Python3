from random import choice

print('19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.\n')
stg1 = input('Digite o nome do aluno 1: ')
stg2 = input('Digite o nome do aluno 2: ')  
stg3 = input('Digite o nome do aluno 3: ')
stg4 = input('Digite o nome do aluno 4: ')
print('O aluno sorteado foi: {}'.format(choice([stg1, stg2, stg3, stg4])))