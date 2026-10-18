print('===== DESAFIO 11 =====')
num1 = float(input('Digite a largura da parede em metros: '))    
num2 = float(input('Digite a altura da parede em metros: '))  
print('A área da parede é {:.2f}m²\nA quantidade de tinta necessária é {:.2f}L'.format(num1 * num2, ((num1 * num2) / 2)))