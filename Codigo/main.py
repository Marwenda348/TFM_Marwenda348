#Importamos archivo de Comprobación
import Comprobar as wl
import IaConnection as Ia
import Whois as Sn
#Solicitamos dominio y lo validamos.
print("Intruduzca el Dominio a escanear")
Input= input()
DominioInput = Input
Whitelist = wl.DominioValido(DominioInput)
Ialist = Ia.Preguntar(DominioInput)

if ( Whitelist >= 1 and Ialist == "Si"):
    #Ia.Preguntar(DominioInput)
    Sn.whois(DominioInput)
else:
    print ("No es un dominio Valido")    