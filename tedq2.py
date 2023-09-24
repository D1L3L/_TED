#Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
# calcule e escreva o custo total da compra.

qnt = int(input("Quantas maçãs você quer? "))

if qnt >= 12:
    preco = 1
    final = float(qnt * preco)
    print(f"O custo de {qnt} maçãs foi de R${final:.2f}")
else:
    preco = 1.30
    final = float(qnt * preco)
    print(f"O preço final foi de R${final:.2f}")