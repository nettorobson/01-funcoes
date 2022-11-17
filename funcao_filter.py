# Filtra um elemento de uma coleção de dados

lista1 = [1, "João", 67, "Pedro", 78.54]
def busca(x):
    return x == 1

print(list(filter(busca,lista1)))


# Otimizando a busca usando o lambda
print(list(filter(lambda x: x == "Pedro",lista1)))