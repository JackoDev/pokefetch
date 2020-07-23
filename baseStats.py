import requests
import json
from genDict import generateDicts


def getBaseStats(name):
    if name:
        URL_STATS = "https://pokeapi.co/api/v2/pokemon/"
        response3 = requests.get(URL_STATS + name)
        # stats_dict = {}

        if response3.status_code == 200:
            response_json3 = json.loads(response3.text)
            stats = response_json3['stats']
            for ability in range(len(stats)):
                abilityName = stats[ability]['stat']['name']
                abilityRange = stats[ability]['base_stat']
                print('\t' + abilityName + ' : ' + str(abilityRange))
            generateDicts(name)
                # stats_dict[abilityName] = abilityRange
            # new_dict = {'name': name, 'Pokemon Id' : id_pokemon, 'weigth' : weigth, 'heigth' : height, 'stats' : stats_dict}
            # my_collection.insert_one(new_dict)
    else:
        print('No data for {}'.format(name))
    
    # print(new_dict)