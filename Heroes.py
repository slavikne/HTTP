import requests
def smartest_hero(list_heroes):
    API_BASE_URL = "https://superheroapi.com/api/2619421814940190/"
    id_heroes = {}
    intelligence_heroes = {}
    list_intel = []
    for hero in list_heroes:
        response = requests.get(API_BASE_URL+'search/'+hero)
        id_heroes[hero] = response.json()['results'][0]['id']
    for hero, id_h in id_heroes.items():
        response_2 = requests.get(API_BASE_URL + id_h+'/powerstats')
        intelligence_heroes[hero] = response_2.json()['intelligence']
        list_intel.append(int(response_2.json()['intelligence']))
    for hero, intel in intelligence_heroes.items():
        if int(intel) == sorted(list_intel)[-1]:
            print(f'Самый умный супергерой - это {hero}')

heroes = ['Hulk', 'Captain America', 'Thanos']
smartest_hero(heroes)