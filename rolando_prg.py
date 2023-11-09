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
# Sukuriu zodyna is dvieju listu, destruktyvu
print('-' * 20)
skoniu_dict = {}
for fruit in listas:
    for taste in pazym:
        skoniu_dict[fruit] = taste
        pazym.remove(taste)
        break
# Printuoju dict:
for key, value in skoniu_dict.items():
    print(key,'->',value)
# Lengvas metodas su dict comprehension
listas = ["Kriaušė", "Obuolys", "Slyva", "Serbentas"]
pazym = ["skanu", "skanu", "neskanu", "neskanu"]
print('-' * 20)
skoniu_dict2 = {listas[i]: pazym[i] for i in range(len(pazym))}
for key, value in skoniu_dict2.items():
    print(key,'->',value)
