import requests
import json
import pymongo
from mongoconection import client, my_db, my_collection
""" This is the module for generate the dicts with the
    fetched info and send them to the mongoDB collection
    on the atlas cloud """


def generateDicts(name):
    """ Method to generate dicts to store the fetched info """
    if name:
        try:
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
                    # loop for find each data stats
                    abilityName = stats[ability]['stat']['name']
                    abilityRange = stats[ability]['base_stat']
                    stats_dict[abilityName] = abilityRange
                    # asignando los key:values para llenar el diccionario
                new_dict = {'name': name, 'Pokemon Id': id_pokemon, 'weigth': weight, 'heigth': height, 'stats': stats_dict}

                my_collection.insert_one(new_dict)
                # sending info to the mongoDB collection
        except:
            print ("Error creating dicts to store info (genDict error)")
    else:
        print('No data for {}'.format(name))
