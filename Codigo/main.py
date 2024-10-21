import Comprobar as wl


print("Intruduzca el Dominio a escanear")
DominioInput = input()
Domain=wl.whitelist(DominioInput)

if Domain :
    print("Se ha registrado su Dominio")
else:
    print("Introduzca un valor valido")  