
# O args vai retornar uma tupla:
def soma (*args):
    print(args)

soma(1,2,43,6,7,7,4,3,)

# 

def soma_total (*args):
    total = 0
    for n in args:
        total += n
    return total

soma_total(1,4,6,7,33,123,3)
a = soma_total(1,2,4,56,67,4)
type(a)

