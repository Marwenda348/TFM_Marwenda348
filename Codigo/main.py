#Importamos archivo de Comprobación
import Comprobar as wl
import IaConnection as Ia
#Solicitamos dominio y lo validamos.
print("Intruduzca el Dominio a escanear")
DominioInput = input()

if (wl.DominioValido(DominioInput)>= 1):
    Ia.Preguntar(DominioInput)
    
else:
    print ("No es un dominio Valido")    