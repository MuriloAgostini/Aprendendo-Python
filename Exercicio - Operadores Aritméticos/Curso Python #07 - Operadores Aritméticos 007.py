larg = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
m1 = float(larg*alt)
area = m1 / 2

print ('Para pintar a parede vai ser necessário {:.2f} litros de tinta'.format(area))
