import shodan
#Importamos la libreria de Shodan y nuestro archivo Componentes donde tenemos la APIkey
from Componentes import ApiShodan
import Mongo as mdb

#Rescatamos la APIkey de Shodan
api = shodan.Shodan(ApiShodan)

# Añadimos una IP que sabemos que tiene vulnerabilidades para ir trabajando en los Json
# y poder extraer la información necesaria.
def Buscar(IP):
    try:    
        #Buscamos por la IP
        ipinfo = api.host(str(IP))

        Ip=ipinfo.get("ip_str")
        Hostname=ipinfo.get("hostnames")
        Dominio=ipinfo.get("domains")
        Puertos=ipinfo.get("ports")
        Vulns=ipinfo.get("vulns") 
        #Probamos si funciona

        Insertar={
            "Dominio": Dominio,
            "Ip" : Ip,
            "Hostname": Hostname,
            "Puertos vuln" : Puertos,
            "Vulnerabilidades" : Vulns
        }
        print(Insertar)
    #mdb.Añadir(Ip,Insertar)
    #mdb.Listartodo(Ip)
    #print (Ip)
#Si no funciona la conexión saltará el error
    except shodan.APIError as e:
        print('Error: {}'.format(e))