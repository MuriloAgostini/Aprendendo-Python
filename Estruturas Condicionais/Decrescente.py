print ('Voce devera informar tres numeros diferentes')

nNumero1 = int(input('Informe o primeiro numero: '))
nNumero2 = int(input('Informe o segundo numero: ' ))
nNumero3 = int(input('Informe o terceiro numero: '))

nMaior = nNumero1
nMeio  = nNumero1
nMenor = nNumero1

if nMaior > nNumero2 and nMaior > nNumero3 :
    if nNumero3   > nNumero2 :
        nMeio   = nNumero3
        nMenor  = nNumero2
    elif nNumero3 < nNumero2 :
        nMeio   = nNumero2
        nMenor  = nNumero3

if nNumero2 > nMaior :
    if nNumero2 > nNumero3 :
        nMaior  = nNumero2
    if nNumero2 < nNumero3 :
        nMaior = nNumero3
        nMeio  = nNumero2

if nNumero3 > nMaior :
    if nNumero3 > nNumero2 :
        nMaior = nNumero3
    if nNumero3 < nNumero2 :
        nMaior = nNumero2
        nMeio  = nNumero3

print ('Os numeros informados em ordem decrescente é : {}, {} e {}' .format (nMaior,nMeio,nMenor))