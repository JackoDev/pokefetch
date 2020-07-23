import pymongo

client = pymongo.MongoClient("mongodb+srv://pokeusuario:pokepassword@pokecluster.z7r13.gcp.mongodb.net/poketest?retryWrites=true&w=majority")
my_db = client.poketest
my_collection = my_db.pokemones

try:
    print("MongoDB version is %s" %
            client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)