import math
oposto = float(input('informe o comprimento do cateto oposto '))
adja = float(input('informe o comprimento do cateto adjacente'))

#Hipotenusa ao quadrado = oposto ao quadrado + adja ao quadrado
hipotenusa = math.sqrt((oposto ** 2) + (adja ** 2))
print ('A hipotenusa do valor informaro é {}' .format(hipotenusa))