from random import randint
numero_de_clientes = 1000
lista_de_avaliacoes = []
while numero_de_clientes > 0:

    numero_de_clientes -= 1

    lista_de_avaliacoes.append(randint(1, 5))

    resposta1 = lista_de_avaliacoes.count(1)
    resposta2 = lista_de_avaliacoes.count(2)
    resposta3 = lista_de_avaliacoes.count(3)
    resposta4 = lista_de_avaliacoes.count(4)
    resposta5 = lista_de_avaliacoes.count(5)

print(f"A quantidade de respostas 1 foi = {resposta1}")
print(f"A quantidade de respostas 2 foi = {resposta2}")
print(f"A quantidade de respostas 3 foi = {resposta3}")
print(f"A quantidade de respostas 4 foi = {resposta4}")
print(f"A quantidade de respostas 5 foi = {resposta5}")

