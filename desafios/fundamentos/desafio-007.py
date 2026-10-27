print('7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.\n')
num1 = float(input('Digite a primeira nota: '))
num2 = float (input('Digite a segunda nota: '))  
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(num1, num2, ((num1 + num2) / 2)))