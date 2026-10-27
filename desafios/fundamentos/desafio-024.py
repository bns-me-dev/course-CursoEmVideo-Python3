print('24 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.\n')
stg = str(input('Digite o nome da cidade: ')).strip()
print('A cidade digitada foi: {}'.format(stg))
print('A cidade começa com "santo"? {}'.format(stg.lower().startswith('santo')))