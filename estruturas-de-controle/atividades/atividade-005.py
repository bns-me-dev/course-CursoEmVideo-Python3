print('===== ATV 05 =====')
nome = str(input('Digite seu nome: ')).strip()

if nome == 'Bruno':
    print('Que nome bonito você tem!')
elif nome == 'Davi' or nome == 'Rebeca' or nome == 'Enzo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Fernanda Thalita Juliana Carla':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')