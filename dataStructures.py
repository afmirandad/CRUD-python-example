import requests
#Lista
#Ejemplo: stopAndres = ['nombre','apellido','color','fruta','ciudad','año','edad']
#stopAndres = ['Andres','Miranda','Azul','Fresas','Bogotá',1900,60]
##Consultar dirección de memoria
#print(id(stopAndres))
##Consultar tipo de estructura de datos
#print(type(stopAndres))
#ciudad = "bucaramanga"
#print(type(ciudad))
#stopAndres[1] = 'Diaz'
#print(stopAndres[1])

#stopAndres.append('millonarios')
#print(stopAndres[7])

#stopAndres.remove('millonarios')
#print(stopAndres)

##Una tupla no se puede modificar!!!!
#stopAndres1 = ('Andres','Miranda','Azul','Fresas','Bogotá',1900,60)
#stopAndres1[1] = 'Diaz'


#Diccionarios - JSON?
#dictCities = {'Nombre':'Andres','Apellido':'Miranda','Color':'Azul','Fruta':'Fresas','Ciudad':'Bogotá','Año':1900,'Edad':60}

#print(dictCities['Nombre'])

"""
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

print(response.json()[0]['name']['official'])
"""

#Conjunto

coordinates1 = {1,2,3,4,4,5,6,23,23,11,0,6,7,3,4,5,5,4,4,444}
coordinates = {1,2,3,4,4,5,6,23,23,11,0}
print(coordinates.intersection(coordinates1))
print(coordinates.union(coordinates1))








