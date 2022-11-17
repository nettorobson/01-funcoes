# Usar o *krwargs simples
def aliquota (**kwargs):
    print(kwargs)

aliquota(iss=3,ir=4.8,csll=2.88,cofins=3,pis=0.65)

# Usar o *kwartgs, loop for e fstring para retornar os impostos incidentes em um orçamento de serviço
def avisoAliquotas(**kwargs):
    for tributo, percent in kwargs.items():
        print(f'Neste orçamento você deverá pagar, a cargo de {tributo}, o percentual de {percent}% sobre o valor total.') # FSTRING 

avisoAliquotas(ISS=3,IR=4.8,CSLL=2.88,COFINS=3,PIS=0.65)