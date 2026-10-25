print('43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:\n    – IMC abaixo de 18,5: Abaixo do Peso\n    – Entre 18,5 e 25: Peso Ideal\n	– 25 até 30: Sobrepeso\n    – 30 até 40: Obesidade\n    – Acima de 40: Obesidade Mórbida\n')
num1 = float(input('Informe o peso em kg: '))
num2 = float(input('Informe a altura em m: '))

num3 = num1 / (num2 ** 2)
if num3 < 18.5:
    print('A pessoa está abaixo do peso ideal.')
elif 18.5 <= num3 < 25:
    print('A pessoa está no peso ideal.')
elif 25 <= num3 < 30:
    print('A pessoa está com sobrepeso.')  
elif 30 <= num3 < 40:
    print('A pessoa está com obesidade.')
else:
    print('A pessoa está com obesidade mórbida.')