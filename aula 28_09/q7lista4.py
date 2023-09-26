compra = float(input("Digite o valor da compra: "))
desconto = float(0)
if compra > 100:
    desconto = float(0.1)
    valor_final = float(compra - (compra * desconto))
    print(f"O valor final é de R${valor_final:.2f},  e teve {desconto*100}% de desconto totalizando R${(compra * desconto):.2f} abatidos.")
elif 50 <= compra <= 100:
    desconto = float(0.05)
    valor_final = compra - (compra * desconto)
    print(f"O valor final é de R${valor_final:.2f}, e teve {desconto*100}% de desconto totalizando R${(compra * desconto):.2f} abatidos.")
else:
    valor_final = compra - (compra * desconto)
    print(f"O valor final é de R${valor_final:.2f}, e não teve desconto. ")