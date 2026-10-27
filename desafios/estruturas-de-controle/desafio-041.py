from datetime import date

print('41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:\n    – Até 9 anos: MIRIM\n    – Até 14 anos: INFANTIL\n    – Até 19 anos: JÚNIOR\n    – Até 25 anos: SÊNIOR\n    – Acima de 25 anos: MASTER\n')
num1 = int(input('Informe o ano do seu nascimento: '))
num2 = date.today().year
num3 = num2 - num1

if num3 <= 9:
    print(f' O atleta tem {num3} anos. Classificação: MIRIM.')
elif 10 <= num3 <= 14:
    print(f' O atleta tem {num3} anos. Classificação: INFANTIL.')
elif 15 <= num3 <= 19:
    print(f' O atleta tem {num3} anos. Classificação: JÚNIOR.')
elif 20 <= num3 <= 25:
    print(f' O atleta tem {num3} anos. Classificação: SÊNIOR.')
else:
    print(f' O atleta tem {num3} anos. Classificação: MASTER.')