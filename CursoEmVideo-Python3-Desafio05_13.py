print('===== DESAFIO 05 =====')
num = float(input('Digite um número: '))
print('O número digitado foi {:.1f} ! \nSeu antecessor é {:.1f} e seu sucessor é {:.1f}'.format(num, (num - 1), (num + 1)))

print('===== DESAFIO 06 =====')
num = float(input('Digite um número: '))
print('O dobro de {:.1f} é {:.1f} \nO triplo de {:.1f} é {:.1f} \nA raiz quadrada de {:.1f} é {:.2f}'.format(num, (num * 2), num, (num * 3), num, (num ** (1/2))))

print('===== DESAFIO 07 =====')
num1 = float(input('Digite a primeira nota: '))
num2 = float (input('Digite a segunda nota: '))  
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(num1, num2, ((num1 + num2) / 2)))

print('===== DESAFIO 08 =====')
num = float(input('Digite um valor em metros: '))
print('O valor digitado em centímetros é {:.0f}cm \nO valor digitado em milímetros é {:.0f}mm'.format((num * 100), (num * 1000)))

print('===== DESAFIO 09 =====')
num = int(input('Digite um número inteiro: '))
print('A tabuada de {} é:'.format(num))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, (num * i)))

print('===== DESAFIO 10 =====')
num = float(input('Digite um valor em reais: R$ '))
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(num, (num / 5.20)))

print('===== DESAFIO 11 =====')
largura = float(input('Digite a largura da parede em metros: '))    
altura = float(input('Digite a altura da parede em metros: '))  
print('A área da parede é {:.2f}m²\nA quantidade de tinta necessária é {:.2f}L'.format(largura * altura, ((largura * altura) / 2)))

print('===== DESAFIO 12 =====')
preco = float(input('Digite o preço do produto: R$ '))
print('O preço do produto com 5% de desconto é R$ {:.2f}'.format(preco - (preco * 0.05)))

print('===== DESAFIO 13 =====')
salario = float(input('Digite o salário do funcionário: R$ '))
print('O salário do funcionário com 15% de aumento é R$ {:.2f}'.format(salario + (salario * 0.15)))