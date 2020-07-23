import requests
import json


def getBaseStats(name):
    if name:
        URL_STATS = "https://pokeapi.co/api/v2/pokemon/"
        response3 = requests.get(URL_STATS + name)
        
        if response3.status_code == 200:
            response_json3 = json.loads(response3.text)

            stats = response_json3['stats']
            for ability in range(len(stats)):
                abilityName = stats[ability]['stat']['name']
                abilityRange = stats[ability]['base_stat']
                print('\t' + abilityName + ' : ' + str(abilityRange)) 
    else:
        print('No data for {}'.format(name))