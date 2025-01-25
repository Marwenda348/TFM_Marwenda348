import shodan
#Importamos la libreria de Shodan y nuestro archivo Componentes donde tenemos la APIkey
from Componentes import ApiShodan
import Mongo as mdb
import IaConnection as Ia
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
        if(Vulns):
            with open(str(IP)+"/Informe Técnico "+str(IP)+".txt", "w") as archivo:
                for vulner in Vulns:
                    archivo.write(Ia.Cve(vulner)+"\n\n------------------\n\n")
                    mdb.Añadir(str(IP),Insertar)
        return Insertar
        
        
        #print("Buscando en la Base de datos los datos relativos a la IP:" + Ip)
      #  mdb.Listartodo(Ip)
#Si no funciona la conexión saltará el error   
    except shodan.APIError as e:
        print('Error: {}'.format(e))



def DNS(Domain):    
    result = api.search(Domain)
    dns=[{}]
    for match in result['matches']:
        Ip=match['ip_str']
        Hostname=match['hostnames'],
        Dominio=match['domains']
        Puertos=match['port']
        Vulns=match('vulns')

        dns.append({
            "Dominio": Dominio,
            "Ip" : Ip, 
            "Hostname": Hostname,
            "Puertos vuln" : Puertos,
            "Vulnerabilidades" : Vulns})
    return dns
    
