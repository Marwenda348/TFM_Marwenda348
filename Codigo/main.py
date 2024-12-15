#Importamos archivo de Comprobación
import Comprobar as wl
import IaConnection as Ia
import sniffer as Sn
import ShodanConnection as Sd
#Solicitamos dominio y lo validamos.
print("Intruduzca el Dominio a escanear")
Input= input()
DominioInput = Input
Whitelist = wl.DominioValido(DominioInput)
Ialist = Ia.Preguntar(DominioInput)
Sd.Buscar(DominioInput)
#if ( Whitelist >= 1 and Ialist == "Si"):
    #Ia.Preguntar(DominioInput)
    #Sn.whois(DominioInput)
    #Sn.Nslookup(DominioInput)
    
#else:
#    print ("No es un dominio Valido")    