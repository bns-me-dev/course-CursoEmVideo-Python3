from datetime import date

print('39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.\n')
stg = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
if stg not in 'MF':
    print('Sexo inválido. Tente novamente.')
elif stg == 'M':

    num1 = int(input('Informe o ano do seu nascimento: '))

    num2 = date.today().year
    num3 = num2 - num1

    if num3 < 18:
        print(f' Você tem {num3} anos. Ainda faltam {18 - num3} anos para o alistamento.')
    elif num3 == 18:
        print(f' Você tem {num3} anos. Está na hora de se alistar!')
    else:
        print(f' Você tem {num3} anos. Deveria ter se alistado a {num3 - 18} ano(s).')
else:
    print('Não é necessário se alistar.')

