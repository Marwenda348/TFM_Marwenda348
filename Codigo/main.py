#Importamos archivo de Comprobación
import Comprobar as wl
import IaConnection as Ia
import sniffer as Sn
import ShodanConnection as Sd
import Mongo as mdb


#Solicitamos dominio y lo validamos.
print("Intruduzca el Dominio a escanear")
Input= input()
DominioInput = Input
Whitelist = wl.DominioValido(DominioInput)
#Ialist = Ia.Preguntar(DominioInput) 
if ( Whitelist >= 1):# and Ialist == "Sí" ):
    try:
        #mdb.Añadir(DominioInput,Sn.whois(DominioInput))
        #mdb.Añadir(DominioInput,Sn.Nslookup(DominioInput))
        Shodan=Sd.Buscar(DominioInput)
        with open("informe"+DominioInput+".txt", "w") as archivo:
            archivo.write(Ia.Informe(Shodan))
    finally:
        print("No se pudo hacer nada")
else:
    print ("No es un dominio Valido")    