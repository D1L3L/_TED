#Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou.
# Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$500,00", 
# caso contrário, imprima "Sem Bônus".

extras = float(input("Digite o número de horas extras realizadas: "))
faltas = float(input("Digite o número de horas que o funcionário faltou: "))
metade = faltas * 0.5
if ((faltas/2) + faltas) <= extras:
    print("Bônus de R$500,00")

else:
    print("Sem Bônus")