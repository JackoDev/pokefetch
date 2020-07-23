import requests
import json

def getWeightAndHeight(name):
    if name:
        URL_POKE = "https://pokeapi.co/api/v2/pokemon/"
        response2 = requests.get(URL_POKE + name)
        
        if response2.status_code == 200:
            response_json2 = json.loads(response2.text)

            id_pokemon = response_json2['id']
            weight = response_json2['weight']
            height = response_json2['height']
            print('Pokemon ID: {}'.format(id_pokemon))
            print('Weight: {}'.format(weight))
            print('Height: {}'.format(height))
    else:
        print('No data for {}'.format(name))