print('27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.\n')
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome é {}\n Primeiro nome: {} \n Último nome: {}'.format(nome, nome.split()[0], nome.split()[-1]))