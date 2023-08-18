nAno = int(input('Informe um ano para verificar se ele foi ou sera bissexto: '))
nBis = nAno / 4

if nBis - int(nBis) == 0 :
    print ('O ano {} é um ano bissexto' .format(nAno))
else :
    print ('O ano {} nao é um ano bissexto ' .format(nAno))