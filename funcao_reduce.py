from functools import reduce
lista = [2,7,10,6,78]

def multi(a,b):
    return a*b

print(reduce(multi,lista))

# Testar o maior valor usando reduce e tbm uma função LAMBDA

lista2 = [30,67,1000,354,51]

testmaior = lambda x,y: x if (x>y) else y
print(reduce(testmaior, lista2))
