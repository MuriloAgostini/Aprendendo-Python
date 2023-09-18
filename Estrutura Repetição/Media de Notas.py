while True:
    print("= Informe as notas dos 4 bimestres")
    nNota1 = int(input("Informe a nota do primeiro bimestre: "))
    nNota2 = int(input("Informe a nota do segundo bimestre: "))
    nNota3 = int(input("Informe a nota do terceiro bimestre: "))
    nNota4 = int(input("Informe a nota do quarto bimestre: "))
    nMedia = (nNota1 + nNota2 + nNota3 + nNota4) / 4

    if nMedia < 7 :
        print (f"Infelizmente voce reprovou, ou é burro ou não se dedicou ! Sua média foi de {nMedia}")
    elif nMedia > 7 :
        print (f"Parabens voce foi aprovado ! Sua Média final foi de {nMedia}")
    
    cContinuar = input("\nVocê deseja consultar outra média ? (S/N)")
    if cContinuar == "S":
        continue
    elif cContinuar == "N":
        print("Obrigado por consultar")
        break
    