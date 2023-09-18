while True:
    nHorastrabalhadas = int(input("Informe o numero de horas trabalhas no ultimo mês "))
    nValorhora        = int(input("Qual o valor por sua hora de trabalho ? "))
    nSalario          = nHorastrabalhadas*nValorhora
    print (f"O seu salario do ultimo mes foi de {nSalario} reais.")

    cContinuar = input("Voce deseja consultar outro salario ? (S/N)")

    if cContinuar == "S":
        continue
    elif cContinuar == "N":
        if nSalario > 3000 :
            print ("Parabens e obrigado por consultar")
        elif nSalario < 900 :
            print ("A pobreza é triste =/ Obrigado por consultar )")
        break
