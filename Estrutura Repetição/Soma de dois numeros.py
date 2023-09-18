while True:
    nNumero1 = int(input("informe um numero: "))
    nNumero2 = int(input("informe um numero para ser somado ao primeiro: "))
    nSoma    = (nNumero1+nNumero2)
    print("A soma dos numeros é {}" .format(nSoma))
    
    cContinuar = input("\nDeseja Continuar ? S/N : ")
    if cContinuar == "S":
        continue
    elif cContinuar == "N":
        print("Obrigado por somar")
        break