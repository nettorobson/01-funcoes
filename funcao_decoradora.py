# Uma função decoradora precisa ter uma função dentro de outra função
# PEP 318 determina que essa é a construção de uma função decoradora

def master(msg):
    def imprime():
        print("Esta é a função decoradora")
        msg()
    return imprime

# Segunda função que vai ser utilizada junto com a decoradora
@master
def funcaoSimples():
    print("Estou chamando a função simples")

# Chamando a função decoradora
# Escreve o "@master" antes da função Simples e roda de novo
# Aí chamando a função simples ela vem as duas.

funcaoSimples()