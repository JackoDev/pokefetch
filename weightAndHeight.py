import requests
import json
""" This is an aditional module with the function to
    obtain the Weight and Heigth of the pokemons """


def getWeightAndHeight(name):
    """ Method to fetch data from other api uri """
    if name:
        try:
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
        except:
            print ("Error fetching data (Weigth & Heigth")
    else:
        print('No data for {}'.format(name))
