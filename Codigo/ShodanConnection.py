import shodan
#Importamos la libreria de Shodan y nuestro archivo Componentes donde tenemos la APIkey
from Componentes import ApiShodan
#Guardaremos la información en Json
import json
#Rescatamos la APIkey de Shodan
api = shodan.Shodan(ApiShodan)

# Añadimos una IP que sabemos que tiene vulnerabilidades para ir trabajando en los Json
# y poder extraer la información necesaria.
try:    
    #Buscamos por la IP
    ipinfo = api.host('172.105.154.45')
    #Guardamos toda la info en un Json
    with open('Total.json', 'w') as file:
        json.dump(ipinfo, file, indent=4)
    #intentamos filtrar por vulnerabilidades
    # for item in ipinfo['vulns']:
    #     Vulnerabilidad="""
    #         Port: {}
    #         Banner: {}
    #         Vulnerabilidad{}
    #         """.format(item['port'], item['data'], item['vulns'])          
    #     with open('Vulns.json', 'w') as file:
    #         json.dump(Vulnerabilidad, file, indent=4)
#Si no funciona la conexión saltará el error
except shodan.APIError as e:
     print('Error: {}'.format(e))
