print('11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.\n')
num1 = float(input('Digite a largura da parede em metros: '))    
num2 = float(input('Digite a altura da parede em metros: '))  
print('A área da parede é {:.2f}m²\nA quantidade de tinta necessária é {:.2f}L'.format(num1 * num2, ((num1 * num2) / 2)))