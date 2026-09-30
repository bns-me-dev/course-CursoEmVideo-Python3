print('===== DESAFIO 15 =====')
num = float(input('Por quantos dias você alugou o carro? '))
num1 = float(input('Quantos km você rodou com o carro? '))
print('O total a pagar é R$ {:.2f}'.format((num * 60) + (num1 * 0.15)))

print('===== DESAFIO 14 =====')
num = float(input('Digite a temperatura em °C: '))
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(num, ((num * 9/5) + 32)))

print('===== DESAFIO 13 =====')
num = float(input('Digite o salário do funcionário: R$ '))
print('O salário do funcionário com 15% de aumento é R$ {:.2f}'.format(num + (num * 0.15)))

print('===== DESAFIO 12 =====')
num = float(input('Digite o preço do produto: R$ '))
print('O preço do produto com 5% de desconto é R$ {:.2f}'.format(num - (num * 0.05)))

print('===== DESAFIO 11 =====')
num1 = float(input('Digite a largura da parede em metros: '))    
num2 = float(input('Digite a altura da parede em metros: '))  
print('A área da parede é {:.2f}m²\nA quantidade de tinta necessária é {:.2f}L'.format(num1 * num2, ((num1 * num2) / 2)))

print('===== DESAFIO 10 =====')
num = float(input('Digite um valor em reais: R$ '))
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(num, (num / 5.20)))

print('===== DESAFIO 09 =====')
num = int(input('Digite um número inteiro: '))
print('A tabuada de {} é:'.format(num))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, (num * i)))

print('===== DESAFIO 08 =====')
num = float(input('Digite um valor em metros: '))
print('O valor digitado em centímetros é {:.0f}cm \nO valor digitado em milímetros é {:.0f}mm'.format((num * 100), (num * 1000)))

print('===== DESAFIO 07 =====')
num1 = float(input('Digite a primeira nota: '))
num2 = float (input('Digite a segunda nota: '))  
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(num1, num2, ((num1 + num2) / 2)))

print('===== DESAFIO 06 =====')
num = float(input('Digite um número: '))
print('O dobro de {:.1f} é {:.1f} \nO triplo de {:.1f} é {:.1f} \nA raiz quadrada de {:.1f} é {:.2f}'.format(num, (num * 2), num, (num * 3), num, (num ** (1/2))))

print('===== DESAFIO 05 =====')
num = float(input('Digite um número: '))
print('O número digitado foi {:.1f} ! \nSeu antecessor é {:.1f} e seu sucessor é {:.1f}'.format(num, (num - 1), (num + 1)))

print('===== DESAFIO 04 =====')
text = input('Digite algo: ')
print('O valor digitado é:', text)
print('O tipo primitivo desse valor é:', type(text))    
print('Só tem espaços?', text.isspace())
print('É um número?', text.isnumeric()) 
print('É alfabético?', text.isalpha())
print('É alfanumérico?', text.isalnum())    
print('Está em maiúsculas?', text.isupper())
print('Está em minúsculas?', text.islower())
print('Está capitalizada?', text.istitle())

print('===== DESAFIO 03 =====')
num1 = int(input('Digite um número '))
num2 = int(input('Digite outro número '))
soma = num1 + num2
print('A soma entre {} e {} é {}!'.format(num1, num2, soma))

print('===== DESAFIO 02 =====')
diaNasc = input('Dia = ')
mesNasc = input('Mes = ')
anoNasc = input('Ano = ')
print('Você nasceu no dia ', diaNasc, 'de', mesNasc, 'de', anoNasc, ' . Correto?')

print('===== DESAFIO 01 =====')
nome = input('Qual o seu nome?')
print('Olá '+ nome + ' ! Prazer em te conhecer!')