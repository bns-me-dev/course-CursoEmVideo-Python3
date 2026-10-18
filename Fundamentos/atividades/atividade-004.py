nome = str(input('Qual o seu nome? ')).strip()

print('Olá {}!'.format(nome) if nome != '' else 'Você não digitou um nome válido.')