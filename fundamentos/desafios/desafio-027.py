print('===== DESAFIO 27 =====')
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome é {}\n Primeiro nome: {} \n Último nome: {}'.format(nome, nome.split()[0], nome.split()[-1]))