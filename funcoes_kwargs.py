def soma (**kwargs):
    print(kwargs)

soma(dia=1,tarde=5,noite=4)

# outro teste, usando a função .items (Trazer, chave+velo, chave+Valor, chave+valor)
# Vamos usar a FSTRINGS (Conceito importante que será muito usado)
def saudacao_dia(**kwargs):
    for periodo_dia, saudacao in kwargs.items():
        print(f'Durante a {periodo_dia} dizemos {saudacao}') # FSTRING

saudacao_dia(manha="bom dia", tarde="boa tarde", noite="vai dormir")






