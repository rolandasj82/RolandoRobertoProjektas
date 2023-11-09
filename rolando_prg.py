listas = ["Kriaušė", "Obuolys", "Slyva", "Serbentas"]
pazym = ["skanu", "skanu", "neskanu", "neskanu"]
print("--- spausdinam lista")
for el in listas:
    print(el)
# Sujungiam listus
bendras = list(zip(listas, pazym))
print(bendras)
# Spausdinam su pridetu tekstu
for v in bendras:
    print(v[0], v[1])
