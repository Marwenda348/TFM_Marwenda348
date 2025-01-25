#Importamos archivo de Comprobación
import Comprobar as wl
import IaConnection as Ia
import sniffer as Sn
import ShodanConnection as Sd
import Mongo as mdb
import os
import Interfaz as inter
#Solicitamos dominio y lo validamos.
#print("Intruduzca el Dominio a escanear")
#Input= input()
#DominioInput = str(Input)
inter.get_ip
DominioInput =inter.ip_address 
Whitelist = wl.DominioValido(str(DominioInput))
Ialist = Ia.Preguntar(str(DominioInput)) 
if ( Whitelist >= 1 and Ialist == "Sí" ):
    if not os.path.exists(str(DominioInput)):
        os.mkdir(str(DominioInput))
    else:
        print(f"La carpeta '{str(DominioInput)}' ya existe.")
    try:
        Sn.whois(str(DominioInput))
        Sn.Nslookup(str(DominioInput))
        Shodan=Sd.Buscar(str(DominioInput))
        with open(str(DominioInput)+"/informe "+str(DominioInput)+".txt", "w") as archivo:
            archivo.write(Ia.Informe(Shodan))
    finally:
        print("Done")
else:
    print ("No es un dominio Valido")    