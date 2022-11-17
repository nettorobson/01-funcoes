animais = ["cachorro", "jacaré", "cavalo"]
animais2 = ("dog", "cat", "bird")
print(list(enumerate(animais)))
print(enumerate(animais2))
# Se não jogar em nenhuma estrutura de dados, ele vai imprimir A MEMORIA DO OBJETO
# POR ISSO É OBRIGADO A CHAMAR O LIST ANTES, mesmo que a variável seja uma lista, tuple ou outra estrutura

type(enumerate(animais))
type(enumerate(animais2))

# iterar com enumerate
# Enumerate como estrutura de dados
for i, valor in enumerate(animais):
    print(i,valor)

for j in enumerate(animais):
    print(j)

# Enumerate com condicionais
for i, valor in enumerate(animais):
    if i > 1:
        break
    else:
        print(valor)
