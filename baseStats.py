import requests
import json
from genDict import generateDicts
""" This is a module with the method to fetch the base-stats
    amounts of each pokemon and call the function for generate
    the dicts to store the info """


def getBaseStats(name):
    """ Method to fetch base-stats and call the genDict function"""
    if name:
        try:
            URL_STATS = "https://pokeapi.co/api/v2/pokemon/"
            response3 = requests.get(URL_STATS + name)

            if response3.status_code == 200:
                response_json3 = json.loads(response3.text)
                stats = response_json3['stats']
                for ability in range(len(stats)):
                    abilityName = stats[ability]['stat']['name']
                    abilityRange = stats[ability]['base_stat']
                    print('\t' + abilityName + ' : ' + str(abilityRange))
                generateDicts(name)
        except:
            print ("Error Fetching data (Base-stats)")
    else:
        print('No data for {}'.format(name))
