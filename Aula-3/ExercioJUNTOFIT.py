print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")

presenca = int(input("Informe a presença do usuário:"))

if presenca == 21:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
elif presenca < 21:
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
else:
    print("VOCÊ JA PARTICIPOU DA CAMPANHA E JA TROUXE UM AMIGO(A)!")

