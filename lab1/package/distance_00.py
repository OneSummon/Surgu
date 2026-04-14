sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def distance(sites: dict):
    distances = {}
    sities_keys = list(sites.keys())

    for i in range(len(sites)):
        next_i = (i + 1) % len(sites)
        
        distance = {"distance" : ((sites[sities_keys[i]][0] - sites[sities_keys[next_i]][0]) ** 2 + (sites[sities_keys[i]][1] - sites[sities_keys[next_i]][1]) ** 2) ** 0.5}
        distances[f"{sities_keys[i]} -> {sities_keys[next_i]}"] = distance

    return distances

# print(distance(sites))