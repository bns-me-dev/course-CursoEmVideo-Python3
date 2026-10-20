print('===== DESAFIO 40 =====')
num1 = float(input('Informe o valor da primeira nota: '))
num2 = float(input('Informe o valor da segunda nota: '))
num3 = (num1 + num2) / 2

if num3 < 5:
    print(f' A média do aluno foi {num3:.1f}. O aluno está REPROVADO.')
elif 5 <= num3 < 7:
    print(f' A média do aluno foi {num3:.1f}. O aluno está de RECUPERAÇÃO.')
else:
    print(f' A média do aluno foi {num3:.1f}. O aluno está APROVADO.')