#Solicite ao usuário um valor numérico, inteiro ou real, e escrever 
#se é positivo ou negativo (considere o valor zero como positivo).

valor = float(input("Digite um valor numérico: "))

if valor < 0:
    print("O valor digitado é negativo")
else:
    print (f"O valor {valor} é positivo")