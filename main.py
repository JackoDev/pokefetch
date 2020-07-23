import requests
import json
from weightAndHeight import getWeightAndHeight
from baseStats import getBaseStats


def getRequestData():
    URL = "https://pokeapi.co/api/v2/evolution-chain/"
    # evoChain = []  # pendiente optimizar para obtener un array y almacenar cada evolucion para evitar los if anidados recorriendo el json con un loop

    print('Please enter an Id')   # se toman los datos del usuario
    input_id = input()

    response = requests.get(URL + str(input_id))  # se adiciona el id al endpoint
    if response.status_code == 200:
        response_json = json.loads(response.text)
        chain = response_json['chain']

        print('*** Evolution chain # {} ***'.format(input_id))
        name0 = chain['species']['name']
        print('Pokemon Name: {}'.format(name0))
        
        getWeightAndHeight(name0)
        print('+ Base Stats:')
        getBaseStats(name0)

        if chain['evolves_to']: 
            name1 = chain['evolves_to'][0]['species']['name']
            print('- Evolves to: ')
            print('Pokemon Name: {}'.format(name1))
            getWeightAndHeight(name1)
            print('+ Base Stats:')
            getBaseStats(name1)

            if chain['evolves_to'][0]['evolves_to']: 
                name2 = chain['evolves_to'][0]['evolves_to'][0]['species']['name']
                print('- Evolves to: ')
                print('Pokemon Name: {}'.format(name2))
                getWeightAndHeight(name2)
                print('+ Base Stats:')
                getBaseStats(name2)
        
                if chain['evolves_to'][0]['evolves_to'][0]['evolves_to']: 
                    name3 = chain['evolves_to'][0]['evolves_to'][0]['evolves_to'][0]['species']['name']
                    print('- Evolves to: ')
                    print('Pokemon Name: {}'.format(name3))
                    getWeightAndHeight(name3)
                    print('+ Base Stats:')
                    getBaseStats(name3)
                else:
                    print('*** End of the evolution chain # {} ***'.format(input_id))
            else:    
                print('*** End of the evolution chain # {} ***'.format(input_id)) 
        else:
            print('*** End of the evolution chain # {} ***'.format(input_id))
    else:
        print('*** ¡Invalid Id! Please Restart the Script and Try again ***') #optimizar para validacion de enteros en el inicio del input


if __name__ == '__main__':
    getRequestData()
    


    
 


    
