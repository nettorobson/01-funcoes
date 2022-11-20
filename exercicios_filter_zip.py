# Exercício FILTER() e ZIP():

# Separar elementos de uma tupla por tipo:

wc = (4, "Sebastian", 7, "Lewis", 2, "Max", 2, "Fernando")

drivers = []
titles = []

def separador():
    for i in wc:
        if type(i) is str:
            drivers.append(i)
        else:
            titles.append(i)
    print(titles)
    print(drivers)

separador()


# Usando FILTER e ZIP para contar quantos pilotos tem mais de 3 títulos:

# ZIP para transformar em um dicionário "chave:piloto valor:títulos":
wc2 = dict(zip(drivers, titles))
print(wc2)

# Filter para contar quantos pilotos tem mais de 3 títulos:
print(len(list(filter(lambda x: x>3, wc2.values()))))