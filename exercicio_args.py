# Criando função com *args simples

def args(*args):
    print(args)

a=args(1,2,43,6,7,7,4,3,15,"abelha", "mariposa")
type(a)

# Usar '*args' e o loop 'for' para retornar apenas os números impar de uma lista:

def impar2(*args):
    total = []
    for n in args:
        if n % 2:
            total.append(n)
        else:
            continue
    return total

b = impar2(1,2,3,4,5,6,7,8,9,10)
type(b)
print(b)