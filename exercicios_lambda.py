# Usando LAMBDA para comparar aliquotas de imposto entre dois anos com tributações diferentes
aliquota_2022 = 0.1433
aliquota_2023 = 0.1233
valorbruto = 5320.98

impostos_2022 = lambda x: x * aliquota_2022
impostos_2023 = lambda x: x * aliquota_2023
impostos_dif = lambda x: (x * aliquota_2022) - (x * aliquota_2023)

print(round((impostos_2022(valorbruto)),2))
print(round((impostos_2023(valorbruto)),2))
print(round((impostos_dif(valorbruto)),2))

# Usando lambda para testar a diferença dos tempos de volta para a melhor volta do dia

d = {'lap1':1.23433, 'lap2':1.229867, 'lap3':1.254440, 'lap4':1.231322, 'lap5':1.26709}

fastest_lap = min(d.values())
print(fastest_lap)

gap_time = lambda x: x - min(d.values()) 
gap_time(d['lap1'])
gap_time(d['lap2'])
gap_time(d['lap3'])

