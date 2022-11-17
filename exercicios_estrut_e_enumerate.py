# Lista
l = [1,2,3,4,5,6,7]

# Tupla
t = (0.87, 0.99, 0.23, 0.44)

# Dicionário
d = {'lap1':1.23433, 'lap2':1.229867, 'lap3':1.254440}

# Usando função ENUMERATE para retornar índices.
print(list(enumerate(l)))
print(list(enumerate(t)))
print(list(enumerate(d)))
print(dict(enumerate(d)))

# Usando ENUMERATE e CONDICIONAIS
# Criando uma lista apenas com os índices das voltas abaixo de '1.2399'
pushlaps = []
laps = dict(enumerate(d))
for lap in laps:
    if lap <= 1.2399:
        pushlaps.append(lap)
    else:
        None
    print(pushlaps)

# Usando enumerate e condicional. 
# Criando uma nova lista só com as voltas ruins, e criando um indice novo para essa lista.
cooldownlaps = list(enumerate(slowlap for slowlap in d.values() if (slowlap > 1.2399)))
print(cooldownlaps)


