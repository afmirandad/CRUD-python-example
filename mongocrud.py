from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from configmongo import config

#Parametros de conexión a mongo Atlas
cliente = MongoClient(config['chainconnection'])
datadb = cliente[config['database']]
tabla = datadb[config['collection']]

def createone(nombre,apellido, ciudad, equipo):
    data = {'nombre':str(nombre),'apellido':str(apellido),'ciudad':str(ciudad),'equipo':str(equipo)}
    newinput = tabla.insert_one(data)
    return newinput.inserted_id

def readone(idval):
    newread = tabla.find_one({'_id':ObjectId(idval)})
    if newread:
        newread['_id'] = str(newread['_id'])
        print(newread)
    else:
        print("No hay datos")

def updateone(parametro,newdata,idval):
    data = {str(parametro):str(newdata)}
    updateone = tabla.update_many({'_id':ObjectId(idval)},{'$set':data})
    readone(idval)

def deleteone(idval):
    newread = tabla.delete_one({'_id': ObjectId(idval)})
    readone(idval)

if __name__ == '__main__':
    validation = createone("pedro","perez","pereira","pereira fc")
    readone(validation)
    updateone('nombre','Ernesto',validation)
    deleteone(validation)
