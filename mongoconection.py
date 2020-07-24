import pymongo
""" This module contains the info for connect and login
    with the mongoDB Atlas cloud, for send the dicts
    with the info fetched for the later use in  the
    web service """


# Atlas mongoDB data login
client = pymongo.MongoClient("mongodb+srv://pokeusuario:pokepassword@pokecluster.z7r13.gcp.mongodb.net/poketest?retryWrites=true&w=majority")
my_db = client.poketest
my_collection = my_db.pokemones

try:
    # For test the mongoDB connection
    print("MongoDB version is %s" %
            client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)
