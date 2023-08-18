print ('Voce deve informar em centimetro o tamanho dos tres lados do triangulo')
nLado1 = int(input('Informe um dos lados do triangulo: '))
nLado2 = int(input('Informe outro lado do triangulo: '))
nLado3 = int(input('Informe outro lado do triangulo: '))

cTipo = 'triangulo'

if nLado1 == nLado2 and nLado1 == nLado3 :
    cTipo = 'Triangulo Equilatero'
elif nLado1 == nLado2 or nLado1 == nLado3 :
    cTipo = 'Triangulo Isósceles'
elif nLado1 != nLado2 and nLado1 != nLado3 :
    cTipo = 'Triangulo Escaleno'

print ('Lados do triangulo informdados {}, {} e {}' .format(nLado1,nLado2,nLado3))
print (cTipo)
