nNumero = int(input('Informe um numero de 1 a 7: '))
cDiadasemana = 'Dia'
if nNumero <= 1 :
    cDiadasemana = 'Domingo'
elif nNumero <= 2 :
    cDiadasemana = 'Segunda-feira'
elif nNumero <= 3 :
    cDiadasemana = 'Terça-feira'
elif nNumero <= 4 :
    cDiadasemana = 'Quarta-feira'
elif nNumero <= 5 :
    cDiadasemana = 'Quinta-feira'
elif nNumero <= 6 :
    cDiadasemana = 'Sexta-feira'
elif nNumero <= 7 :
    cDiadasemana = 'Sabado'
else :
    cDiadasemana = "Nao foi informado um numero de 1 a 7 como solicitado !"

print ('Numero informado: {}' .format(nNumero))
print (cDiadasemana)