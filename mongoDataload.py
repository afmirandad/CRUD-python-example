import requests, json

url = "https://worldcupjson.net/matches"

response = requests.get(url)

#print(json.dumps(response.json()[63],indent=4))

print("Estadio: "+response.json()[63]['venue'])
print("Ganador: "+response.json()[63]['winner'])
print("Perdedor: "+response.json()[63]['away_team_country'])
print("Goles: "+str(response.json()[63]['home_team']['goals'] + response.json()[63]['home_team']['penalties']))



