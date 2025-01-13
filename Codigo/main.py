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
#Ialist = Ia.Preguntar(DominioInput) 
if ( Whitelist >= 1):# and Ialist == "Sí" ):

    #Whois=Sn.whois(DominioInput)
    #Nslookup=Sn.Nslookup(DominioInput)
    Shodan=Sd.Buscar(DominioInput)
    #informacion=[Shodan,Nslookup,Whois]

    with open(DominioInput+".txt", "w") as archivo:
        archivo.write(Ia.Informe(Shodan))

else:
    print ("No es un dominio Valido")    