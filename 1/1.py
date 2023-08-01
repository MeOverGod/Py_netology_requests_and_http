import requests

from pprint import pprint

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

response = requests.get(url)

intelligence_all = []

if response.status_code:
    
    Hulk = 'Hulk'
    Captain_America = 'Captain America'
    Thanos = 'Thanos'
    
    list_intelligence = []
    list_dict_superheroes = []
        
    list_superheroes = response.json()
    for superhero in list_superheroes:
        intelligence = superhero['powerstats']['intelligence']
        if superhero['name'] == Hulk:
            list_intelligence.append(intelligence)
            Hulk_int = dict(Hulk=intelligence)
            list_dict_superheroes.append(Hulk_int)
            continue
        if superhero['name'] == Captain_America:
            list_intelligence.append(intelligence)
            Captain_America_int = dict(Captain_America=intelligence)
            list_dict_superheroes.append(Captain_America_int)
            continue
        if superhero['name'] == Thanos:
            list_intelligence.append(intelligence)
            Thanos_int = dict(Thanos=intelligence)
            list_dict_superheroes.append(Thanos_int)
            continue
    
    for superhero in list_dict_superheroes:
        for key, value in superhero.items():
            if max(list_intelligence) == value:
                print(f'Самый умный супергерой - {key}')