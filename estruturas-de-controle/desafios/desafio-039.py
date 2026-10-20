from datetime import date

print('===== DESAFIO 39 =====')
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

