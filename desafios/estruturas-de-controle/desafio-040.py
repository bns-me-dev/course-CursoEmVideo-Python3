print('40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida\n    – Média abaixo de 5.0: REPROVADO\n    – Média entre 5.0 e 6.9: RECUPERAÇÃO\n    – Média 7.0 ou superior: APROVADO\n')
num1 = float(input('Informe o valor da primeira nota: '))
num2 = float(input('Informe o valor da segunda nota: '))
num3 = (num1 + num2) / 2

if num3 < 5:
    print(f' A média do aluno foi {num3:.1f}. O aluno está REPROVADO.')
elif 5 <= num3 < 7:
    print(f' A média do aluno foi {num3:.1f}. O aluno está de RECUPERAÇÃO.')
else:
    print(f' A média do aluno foi {num3:.1f}. O aluno está APROVADO.')