# Mesclando dicionário

dic_verduras = {1:"cebola", 2:"alface", 3:"repolho", 4:"beterraba"}
dic_frutas = {1:'maçã', 2:'pêra', 3:'laranja'}

mescla = list(zip(dic_verduras, dic_frutas))
print(mescla)

mesclavalores = list(zip(dic_verduras.values(),dic_frutas.values()))
print(mesclavalores)

# Iterar os valores
for p in mesclavalores:
    print(p)

type(mesclavalores)
type(mesclavalores[0])