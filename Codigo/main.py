#Importamos archivo de Comprobación
import Comprobar as wl
import IaConnection as Ia
import sniffer as Sn
import ShodanConnection as Sd
import Mongo as mdb
import os

#Solicitamos dominio y lo validamos.
print("Intruduzca el Dominio a escanear")
Input= input()
DominioInput = Input
Whitelist = wl.DominioValido(DominioInput)
#Ialist = Ia.Preguntar(DominioInput) 
if ( Whitelist >= 1):# and Ialist == "Sí" ):
    if not os.path.exists(DominioInput):
        os.mkdir(str(DominioInput))
    else:
        print(f"La carpeta '{DominioInput}' ya existe.")



    try:
        Sn.whois(str(DominioInput))
        Sn.Nslookup(DominioInput)
        Shodan=Sd.Buscar(DominioInput)
        with open(str(DominioInput)+"/informe"+DominioInput+".txt", "w") as archivo:
            archivo.write(Ia.Informe(Shodan))
    finally:
        print("Done")
else:
    print ("No es un dominio Valido")    