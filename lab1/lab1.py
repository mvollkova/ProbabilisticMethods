from itertools import permutations, combinations
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def permutacje(lista, pocz=0):
    if pocz == len(lista) - 1:
        print(permutacje.counter, ":", tuple(lista))
        permutacje.counter += 1
    else:
        for i in range(pocz, len(lista)):
            lista[pocz], lista[i] = lista[i], lista[pocz]  
            permutacje(lista, pocz + 1)
            lista[pocz], lista[i] = lista[i], lista[pocz] 

def podzbiory_z_powtorzeniami(n, m, start=1, zbior=[]):
    if len(zbior) == m:
        print(podzbiory_z_powtorzeniami.counter, ":", tuple(zbior))
        podzbiory_z_powtorzeniami.counter += 1
        return
    for i in range(start, n + 1):
        podzbiory_z_powtorzeniami(n, m, i, zbior + [i])

N = int(input("Podaj liczbę N: "))
K = int(input("Podaj liczbę K: "))

cities = {
    1: ("Rome", 41.9028, 12.4964, 2873000),
    2: ("Milan", 45.4642, 9.1900, 1366000),
    3: ("Naples", 40.8522, 14.2681, 966144),
    4: ("Turin", 45.0703, 7.6869, 886837),
    5: ("Palermo", 38.1157, 13.3615, 673735),
    6: ("Genoa", 44.4056, 8.9463, 583601),
    7: ("Bologna", 44.4949, 11.3426, 394463),
    8: ("Florence", 43.7696, 11.2558, 380948),
    9: ("Bari", 41.1171, 16.8719, 322511),
    10: ("Catania", 37.5079, 15.0830, 311584),
    11: ("Venice", 45.4408, 12.3155, 261905),
    12: ("Verona", 45.4384, 10.9916, 258765),
    13: ("Messina", 38.1938, 15.5540, 231693),
    14: ("Padua", 45.4064, 11.8768, 210440),
    15: ("Trieste", 45.6495, 13.7768, 204234)
}

city_ids = list(cities.keys())
min_distance = float("inf")
best_path = None

for perm in permutations(city_ids[:N]):
    distance = 0
    for i in range(len(perm)):
        city1 = perm[i]
        city2 = perm[(i + 1) % len(perm)]  
        lat1, lon1 = cities[city1][1:3]
        lat2, lon2 = cities[city2][1:3]
        distance += haversine(lat1, lon1, lat2, lon2)
    
    if distance < min_distance:
        min_distance = distance
        best_path = perm

print("\n3. Najkrótsza trasa:")
for city_id in best_path:
    print(cities[city_id][0], end=" -> ")
print(cities[best_path[0]][0])  
print(f"Długość trasy: {min_distance:.2f} km")

# 4. Znalezienie podzbioru miast, którego populacja jest najbliższa 50% sumy populacji N miast
selected_cities = [cities[i] for i in city_ids[:N]]
total_population = sum(city[3] for city in selected_cities)
target_population = total_population / 2

best_subset = None
best_diff = float("inf")

for r in range(1, N + 1):
    for subset in combinations(selected_cities, r):
        subset_population = sum(city[3] for city in subset)
        diff = abs(subset_population - target_population)
        if diff < best_diff:
            best_diff = diff
            best_subset = subset

print("\n4. Podzbiór miast najbliższy 50% populacji:")
for city in best_subset:
    print(city[0], end=", ")
print(f"\nSuma populacji: {sum(city[3] for city in best_subset)}")
