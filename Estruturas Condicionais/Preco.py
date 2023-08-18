nPreco1 = float(input('Informe o preço do primeiro produto: '))
nPreco2 = float(input('Informe o preço do segundo produto: ' ))
nPreco3 = float(input('Informe o preço do terceiro produto: '))

nMelhorpreco = nPreco1
cProduto = 'Primeiro'

if nPreco2 < nMelhorpreco and nPreco2 < nPreco3 :
    nMelhorpreco = nPreco2
    cProduto = 'Segundo'
elif nPreco3 < nMelhorpreco and nPreco3 < nPreco2 :
    nMelhorpreco = nPreco3
    cProduto = 'Terceiro'

print ('O melhor preço informado foi {}, referente ao {} produto' .format(nMelhorpreco,cProduto))