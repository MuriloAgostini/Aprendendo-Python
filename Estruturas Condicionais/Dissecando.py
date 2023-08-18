nNumero = int(input('Informe um numero menor que 1000: '))
nCentenas = nNumero / 100
nCentenas = int(nCentenas)
nDezenas  = (nNumero -  nCentenas * 100) / 10
nDezenas  = int(nDezenas)
nUnidades = (nNumero - nDezenas * 10) - nCentenas * 100

print ('O numero informado foi {}, o mesmo possui {} centenas, {} dezenas e {} unidades.' .format (nNumero,nCentenas,nDezenas,nUnidades))