print ('Voce vai informar 3 numeros diferentes para ser verificado qual o maior e menor deles')
nNumero1 = int(input('Informe o primeiro numero: '))
nNumero2 = int(input('Informe o segundo numero: '))
nNumero3 = int(input('Informe o terceiro numero: '))

nMenor = nNumero1
nMaior = int(nNumero1)
if nNumero2   > nMaior  and nNumero2 > nNumero3 :
    if nNumero3 < nMaior :
        nMenor  = nNumero3
    nMaior      = nNumero2
elif nNumero3   > nMaior  and nNumero3 > nNumero2 :
    if nNumero2 < nMaior :
        nMenor  = nNumero2
    nMaior      = nNumero3
elif nMaior     > nNumero2 and nMaior  > nNumero3 :
    if nNumero2 > nNumero3 :
        nMenor  = nNumero3
    elif nNumero3 > nNumero2 :
        nMenor  = nNumero2
    else :
        nMenor  = nNumero1
print ('O Maior numero é {} e o Menor numero é {}' .format(nMaior,nMenor))
         
