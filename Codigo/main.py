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
if ( Whitelist >= 1 and Ialist == "Sí." ):
    #Ia.Preguntar(DominioInput)
    #Sn.whois(DominioInput)
    #Sn.Nslookup(DominioInput)
    Sd.Buscar(DominioInput)
else:
    print ("No es un dominio Valido")    