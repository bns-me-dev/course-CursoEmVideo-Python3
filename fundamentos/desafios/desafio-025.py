print('25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.\n')
stg = str(input('informe o seu nome completo: ')).strip()
print('O nome digitado foi: {}'.format(stg))
print('O nome contém "Silva"? {}'.format('silva' in stg.lower()))