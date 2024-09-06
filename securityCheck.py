import requests,json
from pymongo.mongo_client import MongoClient
from configmongo import config
from urllib.parse import urlparse


#Parametros de conexión a mongo Atlas
cliente = MongoClient(config['chainconnection'])
datadb = cliente[config['database']]
tabla = datadb[config['collection']]


def createone(dominio,ip,ciudad, loc, timezone,dataEmails):
    data = {
        'domain':dominio,
        'ip':str(ip),
        'Ciudad':str(ciudad),
        'Localidad':str(loc),
        'Zona horaria':str(timezone),
        'emails': dataEmails
    }
    newinput = tabla.insert_one(data)
    return newinput.inserted_id

def killEmAll(dominio):
    response = requests.get(str("https://networkcalc.com/api/dns/lookup/"+dominio))
    if response.json()["records"] == None:
        ipAddress = "No IP"
        ipresponse = None
    else:

        ipAddress = response.json()["records"]["A"][0]["address"]
        ipresponse = requests.get("https://ipinfo.io/"+str(ipAddress)+"/json")

    ##emails by domain
    requestHunter = requests.get("https://api.hunter.io/v2/domain-search?domain="+str(dominio)+"&api_key=<ingresar su token>")
    requestHunter = requestHunter.json()['data']['emails']
    dataEmails = []
    for i in range(len(requestHunter)):
        dataEmails.append(requestHunter[i]['value'])
        username = requestHunter[i]['value'].split('@')[0]
        responseGithub = requests.get("https://api.github.com/users/"+str(username)+"/events/public")
        if responseGithub.status_code == 304 & len(responseGithub.json()) > 0:
            for i in range(len(responseGithub.json())):
                print(responseGithub.json()[i]['repo']['url'])
    if ipresponse != None:
        createone(dominio, ipAddress, ipresponse.json()["city"], ipresponse.json()["loc"], ipresponse.json()["timezone"],
              dataEmails)


domains = requests.get("https://raw.githubusercontent.com/carloslfu/Startup-Colombia-Empresas/master/datos.json")
for i in range(len(domains.json())):
    if 'webpage' in domains.json()[i]:
        parsed_url = urlparse(domains.json()[i]['webpage'])
        domain = parsed_url.netloc
        if domain.startswith("www."):
            clean_domain = domain[4:]
        else:
            clean_domain = domain
        print(clean_domain)
        killEmAll(clean_domain)

