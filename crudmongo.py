from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from configmongo import config

#Parametros de conexión a mongo Atlas
cliente = MongoClient(config['chainconnection'])
datadb = cliente['vulnsData']
tabla = datadb['softwareByIP']

def createone(nombre,apellido,ciudad,equipo):
    data = {'nombre':str(nombre), 'apellido':str(apellido), 'ciudad':str(ciudad), 'equipo':str(equipo)}
    newinput = tabla.insert_one(data)
    validation = tabla.find_one({'_id':ObjectId(newinput.inserted_id)})
    print(newinput.inserted_id)


def readone():
    newread = tabla.find_one({'_id':ObjectId('66d1dfbcef692062b07389d8')})
    if newread:
        newread['_id'] = str(newread['_id'])
        print(newread)
    else:
        print("No hay datos")

def updateone():
    data = {'apellido':'diaz'}
    updateone = tabla.update_many({'_id':ObjectId('66d1dfbcef692062b07389d8')},{'$set':data})
    readone()

def deleteone():
    newread = tabla.delete_one({'_id': ObjectId('66d1dfbcef692062b07389d8')})
    readone()

if __name__ == '__main__':
    idcreacion = createone("juan","gonzalez","cali","america")