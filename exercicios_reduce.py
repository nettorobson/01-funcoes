# Usando a função REDUCE para calcular o tempo de volta a partir do tempo de cada um dos setores da pista
from functools import reduce
lap1 = (32.3455, 29.1090, 36.9889)
lap2 = (32.4501, 29.1011, 37.4319)

laptime = lambda x,y: x+y
print(reduce(laptime,lap1))/60
print(reduce(laptime,lap2))/60
