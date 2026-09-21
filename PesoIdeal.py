altura=0
massa=0
imc=0
alvomin=0
alvomax=0
while True:
    print("CALCULADORA DE PESO/MASSA IDEAL CONFORME IMC")
    altura = int(input("Qual sua altura? Informe apenas 3 números: "))
    massa = int(input("Qual seu peso/massa? Não informe valores decimais: "))
    imc=massa/((altura*altura)/10000)
    alvomin=((altura*altura)*18.5)/10000
    alvomax=((altura*altura)*24.99)/10000
    print("\n####")
    print(f"Seu IMC é {round(imc,2)}.")
    if imc < 17:
        print(f"Você está MUITO ABAIXO do peso/massa ideal.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    elif imc < 18.5:
        print(f"Você está ABAIXO do peso/massa ideal.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    elif imc < 25:
        print(f"Você está com o peso/massa IDEAL.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    elif imc < 30:
        print(f"Você está ACIMA do peso/massa ideal.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    elif imc < 35:
        print(f"Você está OBESO, procure um médico.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    elif imc < 40:
        print(f"Você está em OBESIDADE SEVERA, procure um médico com URGÊNCIA.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    else:
        print(f"Você está em OBESIDADE MÓRBIDA e correndo RISCO DE MORTE.\nSeu peso/massa ideal é entre {round(alvomin,2)} e {round(alvomax,2)}.")
        print("####\n")
    continuar = input("Deseja continuar? Digite S ou N): ")
    if continuar.lower() != 's':
        break
