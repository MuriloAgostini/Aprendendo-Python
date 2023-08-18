nNumero1 = int(input('Informe um numero: '))
nNumero2 = int(input("Informe outro numero: "))

nMaior = nNumero1
if nMaior  > nNumero2 :
    print ("O Numero {} é o maior numero" .format (nNumero1))
elif nMaior < nNumero2 :
    print ('O numero {} é o maior numero' .format (nNumero2))
elif nMaior == nNumero2 :
    print ('Os numeros informados são iguais')
else :
    print ('Não existe um numero maior entre os valores informados.')

    