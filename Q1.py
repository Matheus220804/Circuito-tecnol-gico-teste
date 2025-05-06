renda = float(input("Insira o valor da sua renda em Rombus:"))
if renda <= 2000.00:
    print("Você está isento de pagar o imposto de renda")
elif renda > 2000.01 and renda <= 3000.00:
    imposto = ( renda * 0.08)
    print(f"Você deve {imposto:.2f} rombus. ")
elif renda > 3000.01 and renda <= 4500.00:
    imposto = (renda * 0.18)
    print(f"Você deve {imposto:.2f} rombus. ")
elif renda > 4500.01:
    imposto = (renda * 0.28)
    print(f"Você deve {imposto:.2f} rombus. ")
