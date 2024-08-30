from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from configmongo import config

#Parametros de conexión a mongo Atlas
cliente = MongoClient(config['chainconnection'])
datadb = cliente['vulnsData']
tabla = datadb['softwareByIP']

data = {'nombre':'andres',
 'apellido':'miranda',
 'ciudad':'bucaramanga',
 'equipo':'millonarios'}

def createone():
    newinput = tabla.insert_one(data)

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
    createone()
    readone()
    updateone()