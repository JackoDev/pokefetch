import requests
import json
import pymongo
from mongoconection import client, my_db, my_collection


def generateDicts(name):
    if name:
        URL_DIC = "https://pokeapi.co/api/v2/pokemon/"
        response4 = requests.get(URL_DIC + name)
        stats_dict = {}

        if response4.status_code == 200:
            response_json4 = json.loads(response4.text)
            stats = response_json4['stats']

            id_pokemon = response_json4['id']
            weight = response_json4['weight']
            height = response_json4['height']

            for ability in range(len(stats)):
                abilityName = stats[ability]['stat']['name']
                abilityRange = stats[ability]['base_stat']
                stats_dict[abilityName] = abilityRange
            new_dict = {'name': name, 'Pokemon Id' : id_pokemon, 'weigth' : weight, 'heigth' : height, 'stats' : stats_dict}
            my_collection.insert_one(new_dict)
    else:
        print('No data for {}'.format(name))
    
    # print(new_dict)