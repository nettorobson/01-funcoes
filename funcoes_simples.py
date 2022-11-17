# Funções são códigos ou blocos criados para executar uma ação
# Sempre que precisarmos executar essa ação chamamos a função def

# Função sem argumento
def oi():
    print("Olá. Oi")

oi()

# Função com parâmetros ou argumentos
def soma(a,b):
    return a+b

soma(1,3)

def soma2(a,b=4):
    return a+b

soma2(1)
soma2(1,7)