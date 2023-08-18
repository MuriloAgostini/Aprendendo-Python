nNota1 = float(input('Informe sua nota do primeiro bimestre: '))
nNota2 = float(input('Informe sua nota do segundo bimestre: '))

nMedia = (nNota1 + nNota2)/2
cFinal = 'Aprovado'

if nMedia < 7 :
    cFinal = 'Reprovado'

print ('Sua media foi {}, portanto voce foi {} no ano letivo !' .format (nMedia,cFinal))