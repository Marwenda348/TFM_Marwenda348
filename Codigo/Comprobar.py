#Importamos libreria de REgex
import re

#Definimos la función a utilizar
def whitelist(self):
#Reccoremos el String introducido
    for i in self:
        #Comprobamos letra a letra que esta en la Whitelist
        Whitelist = re.search(r"[a-zA-Z0-9./]",i)
        #Si no lo esta se devuelve None
        if not Whitelist:
            return None
    #Si llegamos aqui quiere decir que todas las letras estan en el whitelist
    #por lo que podemos devolver el texto como vino
    if Whitelist:
        return self
    
def DominioValido(self):
    Domain=whitelist(self)
    if Domain :
        print("Se ha registrado su Dominio")
    else:
        print("Introduzca un valor valido")  