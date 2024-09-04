import requests
from pymongo.mongo_client import MongoClient
from configmongo import config

url = "https://worldcupjson.net/matches"

response = requests.get(url)
#Parametros de conexión a mongo Atlas
cliente = MongoClient(config['chainconnection'])
datadb = cliente[config['database']]
tabla = datadb[config['collection']]

def createone(estadio,ganador, perdedor, goles):
    data = {'Estadio':str(estadio),'Ganador':str(ganador),'Perdedor':str(perdedor),'Goles totales':str(goles)}
    newinput = tabla.insert_one(data)
    return newinput.inserted_id

goles = response.json()[63]['home_team']['goals'] + response.json()[63]['home_team']['penalties']
createone(response.json()[63]['venue'],response.json()[63]['winner'],response.json()[63]['away_team_country'],goles)




